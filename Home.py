import streamlit as st



st.set_page_config(page_title='Attendance System',layout='wide')

st.header('Attendance System using Face Recognition ')

with st.spinner("Developed by Harsh Vaidya"):
    import face_rec
    
st.success('Model loaded sucesfully')
st.success('Redis db sucessfully connected')