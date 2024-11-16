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
collection = db["datapoints"]

with open("coin_values.txt") as file:
    data = file.read().strip()
    lines = data.split("\n")

    print(lines)

    formatted = []
    for line in lines:
        splitOnColon = line.split(": ")
        time = splitOnColon[0]

        splitOnDash = splitOnColon[1].split(" - ")
        
        coin = splitOnDash[0]
        value = splitOnDash[1]

        print(time, coin, value)

        formatted.append({ "coin": coin, "value": float(value), "time": time })

print(formatted)

collection.insert_many(formatted)
