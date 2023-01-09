import os
from dotenv import load_dotenv
load_dotenv()

DBURL = os.getenv("URL")
API_PASS_KEY = os.getenv("PASS_KEY")