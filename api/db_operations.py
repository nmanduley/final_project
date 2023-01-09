import uuid
import streamlit_authenticator as stauth

from data.connection import users_data, users_pass

def add_new_user(username:str, first_name:str, last_name:str, password):
    user_id = uuid.uuid4()
    # hashed_password = stauth.Hasher(password).generate()
    add_info = {
        "user_id":user_id,
        "username":username,
        "first_name":first_name,
        "last_name":last_name}
    add_password = {
        "user_id":user_id,
        "password":password
    }
    users_data.insert_one(add_info)
    users_pass.insert_one(add_password)
    print('User created successfully')

# Add users
users = ['nmanduley', 'admin']
names = ['Nicolas', 'admin']
lnames = ['Manduley', 'admin']
pwords = ['123456', 'admin123456']
hashed_pwds = stauth.Hasher(pwords).generate()

for (user, name, lname, hash_pwd) in zip(users, names, lnames, hashed_pwds):
    add_new_user(user, name, lname, hash_pwd)


    
# add_new_user('admin', 'admin', 'admin', ['admin123456'])

