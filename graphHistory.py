import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt

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

# Function to fetch asset details by asset symbol
def fetch_asset_details(asset_symbol):
    url = f"{base_url}/{asset_symbol}"
    params = {
        "context": "yourExampleString"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"Request successful for asset symbol: {asset_symbol}")
        data = response.json()
        print(data)  # Debugging line to print the response JSON
        return data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None

# Function to plot the trend on a graph
def plot_trend(data):
    if 'data' in data and 'item' in data['data']:
        asset = data['data']['item']
        latest_rate = asset['latestRate']
        price = float(latest_rate['amount'])
        timestamp = latest_rate['calculationTimestamp']

        # Example data for plotting (replace with actual historical data)
        timestamps = [timestamp - i * 3600 for i in range(24)]
        prices = [price - i * 0.01 for i in range(24)]

        plt.plot(timestamps, prices, marker='o')
        plt.xlabel('Timestamp')
        plt.ylabel('Price (USD)')
        plt.title(f"Price Trend for {asset['assetSymbol']}")
        plt.show()
    else:
        print("The 'item' key is not present in the response.")

# Fetch asset details and plot the trend
asset_symbol = "BTC"
data = fetch_asset_details(asset_symbol)
if data:
    plot_trend(data)