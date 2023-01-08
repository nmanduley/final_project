# import uuid
# import streamlit_authenticator as stauth

# # from bson import json_util
# # from json import loads
# from api.data.connection import users_data, users_pass
# type(users_data)

# def add_new_user(username:str, first_name:str, last_name:str, password:str):
#     user_id = uuid.uuid4()
#     hashed_password = stauth.Hasher(password).generate()
#     add_info = {
#         "user_id":user_id,
#         "username":username,
#         "first_name":first_name,
#         "last_name":last_name}
#     add_password = {
#         "user_id":user_id,
#         "password":hashed_password
#     }
#     users_data.insert_one(add_info)
#     users_pass.insert_one(add_password)
#     return 'User created successfully'


# add_new_user('nmanduley', 'Nicolas', 'Manduley', 'test123')

from api.config import DBURL, API_PASS_KEY
print(API_PASS_KEY, DBURL)