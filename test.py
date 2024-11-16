import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

print(api_key)

# Define the API endpoint and parameters
url = "https://rest.cryptoapis.io/wallet-as-a-service/info/ethereum/sepolia/supported-tokens"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key
}
params = {
    "context": "yourExampleString",
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
    print(data)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
