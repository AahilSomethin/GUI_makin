import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.environ.get('mongodb')

client = MongoClient(connection_string)
db = client['grubz']

