import streamlit as st 
from Home import face_rec
import pandas as pd

st.set_page_config(page_title='Reporting', layout='wide')
st.subheader('Reporting')

name = 'attendance:logs'

def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end)  # extract all data from the redis database
    return logs_list

# tabs to show the info
tab1, tab2, tab3 = st.tabs(['Registered Data', 'Logs', 'Attendance Report'])

with tab1:
    if st.button('Refresh Data'):
        # Retrieve the data from Redis Database
        with st.spinner('Retrieving Data from Redis DB ...'):    
            redis_face_db = face_rec.retrieve_data(name='academy:register')
            st.dataframe(redis_face_db[['Name', 'Role']])

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
            In_Time=pd.NamedAgg('Timestamp', 'min'),
            Out_Time=pd.NamedAgg('Timestamp', 'max')
        ).reset_index()

        report_df['in_time'] = pd.to_datetime(report_df['In_Time'])
        report_df['out_time'] = pd.to_datetime(report_df['Out_Time'])

        report_df['Duration'] = report_df['out_time'] - report_df['in_time']

        # Convert duration to hours and minutes
        report_df['Duration_hours'] = report_df['Duration'].dt.seconds // 3600
        report_df['Duration_minutes'] = (report_df['Duration'].dt.seconds // 60) % 60

        all_dates = report_df['Date'].unique()
        name_role = report_df[['Name','Role']].drop_duplicates().values.tolist()
        date_name_roll_zip = []
        for dt in all_dates:
            for name,role in name_role:
                date_name_roll_zip.append([dt, name, role])
        st.dataframe(report_df[['Date', 'Name', 'Role', 'In_Time', 'Out_Time', 'Duration_hours', 'Duration_minutes']])

