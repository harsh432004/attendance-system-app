import os
import streamlit as st
from dotenv import load_dotenv
import requests
from urllib.parse import urlencode

# Load environment variables
load_dotenv()

# Auth0 settings
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID')
AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET')
AUTH0_CALLBACK_URL = os.getenv('AUTH0_CALLBACK_URL')
AUTH0_AUTHORIZATION_URL = f'https://{AUTH0_DOMAIN}/authorize'
AUTH0_TOKEN_URL = f'https://{AUTH0_DOMAIN}/oauth/token'
AUTH0_USERINFO_URL = f'https://{AUTH0_DOMAIN}/userinfo'

def redirect_to_auth0():
    """Redirect to Auth0 login."""
    params = {
        'client_id': AUTH0_CLIENT_ID,
        'redirect_uri': AUTH0_CALLBACK_URL,
        'response_type': 'code',
        'scope': 'openid profile email',
    }
    auth_url = f'{AUTH0_AUTHORIZATION_URL}?{urlencode(params)}'
    st.markdown(
        f'<a href="{auth_url}" target="_self" style="text-decoration: none;">'
        '<button style="background-color: #4CAF50; color: white; border: none; '
        'padding: 10px 20px; font-size: 16px; cursor: pointer;">Login with Auth0</button></a>',
        unsafe_allow_html=True
    )

def handle_callback():
    """Handle callback from Auth0 and process the authorization code."""
    query_params = st.query_params  # Updated for compatibility
    # print("query_params----------------------------->",query_params)
    code = query_params.get('code', [None])  # Retrieve the "code" parameter
    # print("code----------------------------->",code)

    if code:
        # Exchange the authorization code for tokens
        response = requests.post(
            AUTH0_TOKEN_URL,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'client_id': AUTH0_CLIENT_ID,
                'client_secret': AUTH0_CLIENT_SECRET,
                'code': code,
                'redirect_uri': AUTH0_CALLBACK_URL,
                'grant_type': 'authorization_code',
            },
        )

        if response.status_code != 200:
            st.error("Failed to exchange code for token. Please try again.")
            return

        response_json = response.json()
        # print("response_json----------------------------->",response_json)

        access_token = response_json.get('access_token')

        if not access_token:
            st.error("Failed to retrieve access token. Please try again.")
            return

        # Fetch user info
        user_info_response = requests.get(
            AUTH0_USERINFO_URL,
            headers={'Authorization': f'Bearer {access_token}'},
        )

        if user_info_response.status_code != 200:
            st.error("Failed to fetch user info. Please check your Auth0 configuration.")
            return

        try:
            user_info = user_info_response.json()
            st.session_state['user'] = user_info
            st.session_state['access_token'] = access_token
        except requests.exceptions.JSONDecodeError:
            st.error("Failed to decode user info response as JSON.")
    else:
        st.warning("Authorization code not found. Please log in again.")

def is_logged_in():
    """Check if the user is logged in."""
    return 'user' in st.session_state

def logout():
    """Log out the user."""
    st.session_state.clear()  # Clear session state
    logout_url = f"https://{AUTH0_DOMAIN}/v2/logout?client_id={AUTH0_CLIENT_ID}&returnTo={AUTH0_CALLBACK_URL}"
    st.markdown(
        f'<a href="{logout_url}" target="_self" style="text-decoration: none;">'
        '<button style="background-color: #FF6347; color: white; border: none; '
        'padding: 10px 20px; font-size: 16px; cursor: pointer;">Logout</button></a>',
        unsafe_allow_html=True
    )
