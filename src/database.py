import streamlit as st

import itertools
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["HackShef9"]
coins_collection = db["coins"]
datapoints_collection = db["datapoints"]

# @st.cache_resource
def fetch_coin_metadata():
    metadata = list(coins_collection.find({}, {'_id': False}))

    for coin in metadata:
        coin["image_b64"] = "data:image/png;base64," + coin["image_b64"]

    return metadata

def fetch_coin_datapoints():
    return list(datapoints_collection.find({}))

def fetch_joined_coin_datapoints():
    metadata = fetch_coin_metadata()

    for coin in metadata:
        coin["datapoints"] = list(datapoints_collection.find({"coin": coin["name"]}, {"_id": 0, "coin": 0}))

    return metadata
