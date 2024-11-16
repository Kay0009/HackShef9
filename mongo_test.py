from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aarmes1:BPFD90m1IfLC9rSz@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["HackShef9"]
collection = db["coins"]

data = {"name":"coin1", "image":"test1"}
collection.insert_one(data)