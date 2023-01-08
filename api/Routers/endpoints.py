from fastapi import APIRouter
from ..data.connection import users_data, users_pass
from ..config import API_PASS_KEY, DBURL

from bson import json_util
from json import loads

router = APIRouter()

testvar = DBURL
@router.get("/printkey")
def get_key():
    return {"Test": testvar}


# # endpoints
# Get data (id, first name, last name) of a user using the username
@router.get("/user/{username}")
def get_names(username:str):
    filt = {"username":username}
    project = {"_id":0}
    user_info = users_data.find(filt, project)
    user_info = list(user_info)[0]
    if len(user_info) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(user_info))

# Get all first names
@router.get("/first_names")
def get_all_usernames():
    filt = {}
    project = {"_id":0, "first_name":1}
    all_first_names = users_data.find(filt, project)
    all_first_names = list(all_first_names)
    if len(all_first_names) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(all_first_names))

# Get all users
@router.get("/users")
def get_all_usernames():
    filt = {}
    project = {"_id":0, "username":1}
    all_users = users_data.find(filt, project)
    all_users = list(all_users)
    if len(all_users) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(all_users))

# Get all password hashes
@router.get("/hashes/temporalpass")
def get_all_hashes():
    filt = {}
    project = {"_id":0, "password":1}
    all_passwords = users_pass.find(filt, project)
    all_passwords = list(all_passwords)
    if len(all_passwords) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(all_passwords))

# Get user images
@router.get("/images/{username}")
def get_all_hashes(username:str):
    filt = {"username":username}
    project = {"_id":0, "images":1}
    all_images = users_pass.find(filt, project)
    all_images = list(all_images)
    if len(all_images) == 0:
        return {"Error":"Empty data or no data available"}
    return loads(json_util.dumps(all_images))