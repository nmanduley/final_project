import streamlit as st
import streamlit_authenticator as stauth
import requests

# Title
st.set_page_config(page_title="BDML Final Project", layout="wide")

# # Authentication test
# test_name = ["Nicolas", "Alejandro"]
# test_username = ["admin", "admin2"]
# test_pass = ["12345", "test123"]
# hashed_password = stauth.Hasher(test_pass).generate()

api_url = 'http://127.0.0.1:8000'
all_names = requests.get(f"{api_url}/all_first_names").json()
all_usernames = requests.get(f"{api_url}/all_users").json()
all_passwords = requests.get(f"{api_url}/all_hashes/temporalpass").json()


authenticator = stauth.Authenticate(all_names, all_usernames, all_passwords,
'NM_final_project', 'cookie_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username and/or password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    # Header
    with st.container():
        st.subheader("CORE Code School")
        st.title("Final Project: BDML Bootcamp")
        st.write("Nicolas Manduley")
    
    # Body
    with st.container():
        st.write('---')
        st.header("Facial authentication protocol")
        
        # Sidebar
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome, {name}")
        chosen_db = st.sidebar.radio('Seleccionar base de datos:', \
            options=['Casos confirmados', 'Muertes', 'Recuperados'])