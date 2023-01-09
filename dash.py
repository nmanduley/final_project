import streamlit as st
import cv2
import os
from app.dash_functions import load_facial_recognition_model, verify, cut_frame, create_authenticator, get_auth_prompt
from api.config import API_PASS_KEY

# Parameters
PIC_TIMER = 5 # seconds
img_path = os.path.join('facial_recognition', 'app_data', 'input_images')

# Title
st.set_page_config(page_title="BDML Final Project", layout="wide")

# User authentication
pass_key = API_PASS_KEY
authenticator = create_authenticator(pass_key)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username and/or password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")

# Load model
model = load_facial_recognition_model()

if authentication_status:
    # Header
    st.title("Final Project: BDML Bootcamp")
    st.subheader("CORE Code School")
    st.write("Nicolas Manduley")
    
    # Body
    st.write('---')
    st.header("Facial authentication protocol")
    start_camera = st.button('Start Camera')

    # Sidebar
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome, {name}")

    # Camera
    st.write('---')
    if start_camera:
        # Start camera
        FRAME_WINDOW = st.image([])
        cap = cv2.VideoCapture(0)
        n = PIC_TIMER*24
        st.write("Verifying in 5 seconds.")
        st.write("Please place yourself in front of the camera.")
        while n > 0:
            ret, raw_frame = cap.read()
            frame = cut_frame(raw_frame)                
            FRAME_WINDOW.image(frame)
            n -= 1
            # if n%24 == 0:
            #     st.write(n/24+1)
        # Release the webcam
        cap.release()
        cv2.destroyAllWindows()
        cv2.imwrite(os.path.join(img_path, 'input_image.jpg'), frame)

        # Apply verification function
        results, verified = verify(model, 0.8, 0.8)

        # Display authentication status
        prompt = get_auth_prompt(verified)
        st.caption(prompt, unsafe_allow_html=True)
                

        # if cv2.waitKey(1) & stop_camera:
        #     break
        

        # # else:
        # #     st.write('Camera stopped')
     
        # st.write(verified)


        