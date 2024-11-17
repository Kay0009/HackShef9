from time import sleep
import requests
from dotenv import load_dotenv
import os
import base64
from PIL import Image
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

print(api_key)

def get_all_asset_symbols():
# Define the API endpoint and parameters
    url = "https://rest.cryptoapis.io/market-data/assets/supported"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key
    }
    params = {
        "context": "HackShef9",
        "assetType": "crypto",
        "limit": 50,
        "offset": 0
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check the response status
    if response.status_code == 200:
        print("Request successful!")
        # Parse and print the response JSON
        data = response.json()
        items = data["data"]["items"]
        asset_symbols = []
        for i in items:
            asset_symbols.append(i["assetSymbol"])

        return asset_symbols
    
    else:
        return(f"Request failed with status code {response.status_code}: {response.text}")


def get_asset_images(asset):
    
    url = f"https://rest.cryptoapis.io/market-data/assets/{asset}"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key
    }
    params = {
        "context": "HackShef9"
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check the response status
    if response.status_code == 200:
        print("Request successful!")
        # Parse and print the response JSON
        data = response.json()
        image_b64 = data["data"]["item"]["assetLogo"]["imageData"]
        return image_b64
            

    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        

def display_image(b64):
    # Decode the Base64 string
    image_data = base64.b64decode(b64)

    # Convert the bytes data to a PIL image
    image = Image.open(BytesIO(image_data))

    # Display the image
    image.show()




from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["HackShef9"]
collection = db["coins"]

asset_symbols = (get_all_asset_symbols())
print(asset_symbols)


for asset in asset_symbols:
    sleep(1)
    b64 = get_asset_images(asset)
    print(b64)
    result = collection.update_one(
    {"name": asset}, 
    {"$set": {"image_b64": b64}}  
    )

    # Print the result
    if result.matched_count > 0:
        print(f"Document updated. Modified count: {result.modified_count}.")
    else:
        print("No document found with name")


