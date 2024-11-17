from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["HackShef9"]
collection = db["coins"]

result = collection.update_many(
    {},  # Match all documents
    {"$set": {"24hr_change": ""}}  # Add the "image_b64" field with an empty string
)

# Print the result
print(f"Modified {result.modified_count} documents.")