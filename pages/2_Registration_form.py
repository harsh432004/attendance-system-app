import streamlit as st
from Home import face_rec
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
import streamlit.components.v1 as components  # For embedding TinyMCE

# Initialize the registration form
st.subheader('Registration Form')
registration_form = face_rec.RegistrationForm()

# Step 1: Collect person's name and role
person_name = st.text_input(label='Name', placeholder='First & Last Name')
role = st.selectbox(label='Select your Role', options=(
    'Student',
    'High Authority',
    'Teaching Faculty',
    'Non-Teaching Faculty'
))

# Step 2: Add a TinyMCE editor for a bio or additional details
st.markdown("### Bio / Additional Information")
tinymce_code = """
<script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js" referrerpolicy="origin"></script>
<script>
  tinymce.init({
    selector: '#bio_editor',
    plugins: 'lists link image code',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist outdent indent | link image | code',
    height: 300
  });
</script>
<textarea id="bio_editor" name="bio"></textarea>
"""
components.html(tinymce_code, height=400)

# Step 3: WebRTC for facial registration
def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')  # 3D array BGR
    reg_img, embedding = registration_form.get_embedding(img)

    if embedding is not None:
        with open('face_embedding.txt', mode='ab') as f:
            np.savetxt(f, embedding)

    return av.VideoFrame.from_ndarray(reg_img, format='bgr24')


webrtc_streamer(
    key='registration',
    video_frame_callback=video_callback_func,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)

# Step 4: Handle form submission
if st.button('Submit'):
    # Collect data from TinyMCE
    bio_content = st.experimental_get_query_params().get("bio", [""])[0]
    
    if not person_name.strip():
        st.error('Name cannot be empty or spaces')
    elif not bio_content.strip():
        st.error('Bio cannot be empty. Please add some information.')
    else:
        return_val = registration_form.save_data_in_redis_db(person_name, role, bio_content)
        if return_val == True:
            st.success(f"{person_name} registered successfully")
        elif return_val == 'name_false':
            st.error('Please enter the name: Name cannot be empty or spaces')
        elif return_val == 'file_false':
            st.error('face_embedding.txt is not found. Please refresh the page and execute again.')
