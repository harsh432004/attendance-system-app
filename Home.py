import streamlit as st
from auth import redirect_to_auth0, handle_callback, is_logged_in, logout

st.set_page_config(page_title='Attendance System', layout='wide')

def main():

    st.title("Attendance System with Auth0 Authentication")

    # Handle Auth0 callback
    if 'code' in st.query_params:
        handle_callback()

    # Check if the user is logged in
    if is_logged_in():
        user = st.session_state['user']
        st.success(f"Welcome, {user.get('name', 'User')}!")

        logout()   #It will display logout button and onclick logout functionality

        # st.success("Model loaded successfully.")
        # st.success("Redis DB connected successfully.")
    else:
        st.warning("To access this site, please log in.")
        redirect_to_auth0()

if __name__ == "__main__":
    main()
