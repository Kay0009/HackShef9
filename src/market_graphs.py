import streamlit as st
import pandas as pd
import plotly.express as px
import database

# Fetch data from the collection using database.py
data = database.fetch_coin_datapoints()

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