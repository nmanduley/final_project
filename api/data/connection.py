from pymongo import MongoClient
# from bson import json_util
# from json import loads
from config import DBURL
import certifi

ca = certifi.where()
client = MongoClient(DBURL, tlsCAFile=ca, uuidRepresentation='standard')

db = client.get_database("users")
users_data = db["database"]
users_pass = db["passwords"]

# def find_collection(collection, filter={}, project={"_id": 0}):
#     return db[collection].find(filter, project)

# def paginate(page=0, per_page=10):
#     def inner(mongodb_cursor):
#         data = mongodb_cursor.limit(per_page).skip(per_page*page)
#         return {
#             "page": page,
#             "results": loads(json_util.dumps(data))
#         }
#     return inner