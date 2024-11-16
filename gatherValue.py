import requests
import schedule
from dotenv import load_dotenv
import os
from datetime import datetime
import time
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Load environment variables from .env file
load_dotenv()

# Access all API keys
api_keys = [
    os.getenv("API_KEY1"),
    os.getenv("API_KEY2"),
    os.getenv("API_KEY3"),
    os.getenv("API_KEY4"),
    os.getenv("API_KEY5"),
    os.getenv("API_KEY6"),
    os.getenv("API_KEY7")
]

# Function to get the next API key
api_key_index = 0
def get_next_api_key():
    global api_key_index
    api_key = api_keys[api_key_index]
    api_key_index = (api_key_index + 1) % len(api_keys)
    return api_key

# Define the API endpoint
base_url = "https://rest.cryptoapis.io/v2/market-data/assets"

database_uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"

# Function to fetch supported assets
def fetch_supported_assets():
    with open("asset_list.txt", "r") as file:
        data = json.load(file)
        print("Loaded supported assets from asset_list.txt")
        return data

# Function to fetch asset details by asset symbol
def fetch_asset_details(asset_str):
    url = f"{base_url}/{asset_str}"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": get_next_api_key()
    }
    response = requests.get(url, headers=headers)
    time.sleep(1.001)

    if response.status_code == 200:
        print(f"Request successful for asset symbol: {asset_str}")
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    supported_assets = fetch_supported_assets()

    # Connect to the database
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
    datapoints_collection = db["datapoints"]
    coins_collection = db["coins"]

    def fetch_and_store_data():
        for asset in supported_assets:
            asset_symbol = asset.get('assetSymbol')

            if asset_symbol:
                data = fetch_asset_details(asset_symbol)
                if data:
                    latest_rate = data['data']['item']['latestRate']
                    price = float(latest_rate['amount'])
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(price, asset_symbol, timestamp)
                    datapoint = {"coin": asset_symbol, "value": price, "time": timestamp}

                    change = data["data"]["item"]["specificData"]["24HoursPriceChangeInPercentage"]
                    print(change)
                    result = coins_collection.update_one(
                    {"name": asset_symbol}, 
                    {"$set": {"24hr_change": change}}  
                    )

                    datapoints_collection.insert_one(datapoint)
                    print("Successfully added datapoint to the database")
                else:
                    print(f"Symbol not found in asset: {asset}")

    # Schedule the task to run every minute
    schedule.every(4).minutes.do(fetch_and_store_data)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)