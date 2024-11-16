import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB Atlas
database_uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"
client = MongoClient(database_uri, server_api=ServerApi('1'))

# Access the database and collection
db = client["HackShef9"]
datapoints_collection = db["datapoints"]

# Fetch data from the collection
data = list(datapoints_collection.find())

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Convert timestamp to datetime
df['time'] = pd.to_datetime(df['time'])

# Streamlit visualization
st.title("Crypto Coin Values Over Time")

# Select coin
coins = df['coin'].unique()
selected_coin = st.selectbox("Select a coin", coins)

# Filter data for the selected coin
coin_data = df[df['coin'] == selected_coin]

# Create a line chart
fig = px.line(coin_data, x='time', y='value', title=f'{selected_coin} Value Over Time')

# Display the chart
st.plotly_chart(fig)