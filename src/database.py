import streamlit as st

import itertools
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

@st.cache_resource
def get_client():
    uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client["HackShef9"]

def fetch_coin_metadata():
    metadata = list(get_client()["coins"].find({}, {'_id': False}))

    for coin in metadata:
        coin["image_b64"] = "data:image/png;base64," + coin["image_b64"]

    return metadata

def fetch_coin_datapoints():
    return list(get_client()["datapoints"].find({}))

def fetch_joined_coin_datapoints():
    metadata = fetch_coin_metadata()

    for coin in metadata:
        coin["datapoints"] = list(get_client()["datapoints"].find({"coin": coin["name"]}, {"_id": 0, "coin": 0}))

    return metadata
