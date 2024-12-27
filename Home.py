import streamlit as st
from auth import authenticator
st.set_page_config(page_title='Attendance System',layout='wide')



if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.write(f'Welcome *{st.session_state["name"]}*')



    st.header('Attendance System using Face Recognition')

    st.success('Model loaded sucesfully')
    st.success('Redis db sucessfully connected')

else:
    authenticator.login('Login', 'main')

