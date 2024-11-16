import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import schedule
import time
import json

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Define the API endpoint and headers
base_url = "https://rest.cryptoapis.io/v2/market-data/assets"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key
}

# Function to fetch supported assets
def fetch_supported_assets():
    with open("asset_list.txt", "r") as file:
        data = json.load(file)
        print("Loaded supported assets from asset_list.txt")
        return data

# Function to fetch asset details by asset symbol
def fetch_asset_details(asset_str):
    url = f"{base_url}/{asset_str}"
    response = requests.get(url, headers=headers)
    time.sleep(1.001)

    if response.status_code == 200:
        print(f"Request successful for asset symbol: {asset_str}")
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None

# Function to fetch and store asset values
def fetch_and_store_asset_values():
    supported_assets = fetch_supported_assets()
    with open("coin_values.txt", "a") as file:
        for asset in supported_assets:
            asset_symbol = asset.get('assetSymbol')
            if asset_symbol:
                data = fetch_asset_details(asset_symbol)
                if data:
                    latest_rate = data['data']['item']['latestRate']
                    price = float(latest_rate['amount'])
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    file.write(f"{timestamp}: {asset_symbol} - {price}\n")
            else:
                print(f"Symbol not found in asset: {asset}")

# Schedule the task to run every minute
schedule.every(4).minutes.do(fetch_and_store_asset_values)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)