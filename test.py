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


def get_asset_images(asset_symbols):
    for asset in asset_symbols:
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
            print(image_b64)
            display_image(image_b64)

        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
        


def display_image(b64):
    # Decode the Base64 string
    image_data = base64.b64decode(b64)

    # Convert the bytes data to a PIL image
    image = Image.open(BytesIO(image_data))

    # Display the image
    image.show()

# asset_symbols = (get_all_asset_symbols())
# print(asset_symbols[:3])

get_asset_images(["BTC"])


