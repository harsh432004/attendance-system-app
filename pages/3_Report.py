import streamlit as st
from Home import face_rec
import pandas as pd

st.set_page_config(page_title='Reporting', layout='wide')
st.subheader('Reporting')

name = 'attendance:logs'

def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end)  # extract all data from the redis database
    return logs_list

tab1, tab2, tab3 = st.tabs(['Registered Data', 'Logs', 'Attendance Report'])

with tab1:
    if st.button('Refresh Data'):
        with st.spinner('Retrieving Data from Redis DB ...'):
            redis_face_db = face_rec.retrieve_data(name='academy:register')
            if redis_face_db:
                st.dataframe(pd.DataFrame(redis_face_db, columns=['Name', 'Role']))

with tab2:
    if st.button('Refresh Logs'):
        st.write(load_logs(name=name))

with tab3:
    st.subheader('Attendance Report')
    logs_list = load_logs(name=name)

    if logs_list:
        convert_byte_to_string = lambda x: x.decode('utf-8')
        logs_list_string = list(map(convert_byte_to_string, logs_list))
        split_string = lambda x: x.split('@')
        logs_nested_list = list(map(split_string, logs_list_string))
        logs_df = pd.DataFrame(logs_nested_list, columns=['Name', 'Role', 'Timestamp'])
        logs_df['Timestamp'] = pd.to_datetime(logs_df['Timestamp'])
        logs_df['Date'] = logs_df['Timestamp'].dt.date

        report_df = logs_df.groupby(by=['Date', 'Name', 'Role']).agg(
            In_time=pd.NamedAgg('Timestamp', 'min'),
            Out_time=pd.NamedAgg('Timestamp', 'max')
        ).reset_index()

        report_df['In_time'] = pd.to_datetime(report_df['In_time'])
        report_df['Out_time'] = pd.to_datetime(report_df['Out_time'])

        # Calculate duration in hours and minutes
        report_df['Duration'] = (report_df['Out_time'] - report_df['In_time']).dt.total_seconds() / 3600
        report_df['Duration'] = report_df['Duration'].apply(lambda x: '{:0>2}:{:0>2}'.format(int(x), int((x - int(x)) * 60)))
        
        # Calculate duration seconds and hours
        report_df["Duration_seconds"] = (report_df['Out_time'] - report_df['In_time']).dt.total_seconds()
        report_df["Duration_hours"] = report_df["Duration_seconds"] / 3600

        # Add Status column based on Duration_seconds
        report_df['Status'] = report_df['Duration_seconds'].apply(lambda x: 'Present' if x >= 30 * 60 else 'Absent')

        # Display the DataFrame with Status column after Duration_seconds and Duration_hours
        st.dataframe(report_df[['Date', 'Name', 'Role', 'In_time', 'Out_time', 'Duration_seconds', 'Duration_hours', 'Status']])
