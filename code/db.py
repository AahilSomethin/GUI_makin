import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.environ.get('mongodb')

client = MongoClient(connection_string)
db = client["cinema"]
collection = db["bookings"]

try:
    names = client.list_database_names()
    print(names)
    print("Ping has been successful, connection secured")

    with open('bookings.txt') as f:
        lines = f.read().split('\n')

    booking_dict = {}
    for line in lines:
        if ':' in line:
            key, value = line.strip().split(': ')
            booking_dict[key] = value
        else:
            print(f"Warning: Skipping line '{line}' because it doesn't contain a colon.")

    collection.insert_one(booking_dict)


except Exception as e:
        print(f"there was an error in communication with the DB{e}")


except Exception as e:
    print(e)







