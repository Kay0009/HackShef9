import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

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

# List of asset symbols to track
asset_symbols = ["BTC", "ETH", "LTC"]  # Example asset symbols

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
        # Write data to a text file
        with open("coin_values.txt", "a") as file:
            file.write(f"{datetime.now()}: {asset_symbol} - {data}\n")
        return data
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None

# Function to extract historical data from the response
def extract_historical_data(data):
    if 'data' in data and 'item' in data['data']:
        asset = data['data']['item']
        latest_rate = asset['latestRate']
        price = float(latest_rate['amount'])
        timestamp = latest_rate['calculationTimestamp']

        # Example data for plotting (replace with actual historical data)
        timestamps = [timestamp - i * 3600 for i in range(24)]
        prices = [price - i * 0.01 for i in range(24)]

        return timestamps, prices
    else:
        print("The 'item' key is not present in the response.")
        return [], []

# Initialize a DataFrame to store historical data
df = pd.DataFrame()

# Fetch and store historical data for each asset symbol
for asset_symbol in asset_symbols:
    data = fetch_asset_details(asset_symbol)
    if data:
        timestamps, prices = extract_historical_data(data)
        if prices:
            df[asset_symbol] = prices
        else:
            print(f"No data available for {asset_symbol}")

# Check if DataFrame is populated correctly
print(df)

# Plot the data using subplots
fig, axs = plt.subplots(len(asset_symbols), 1, figsize=(10, 8))

for i, asset_symbol in enumerate(asset_symbols):
    if asset_symbol in df:
        axs[i].plot(df.index, df[asset_symbol], marker='o')
        axs[i].set_title(f"Price Trend for {asset_symbol}")
        axs[i].set_xlabel('Timestamp')
        axs[i].set_ylabel('Price (USD)')
    else:
        print(f"No data to plot for {asset_symbol}")

plt.tight_layout()
plt.show()