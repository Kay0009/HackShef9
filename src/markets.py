import database
import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

st.title("Markets")
st.write("Check out the most stagnant and failing markets here.")
st.write("Our analysts recommend that new investors start with coins with an evaluation less than 1 USD.")

coin_data = database.fetch_joined_coin_datapoints()

for coin in coin_data:
    coin["exchange"] = coin["datapoints"][-1]["value"]
    coin["trend"] = [datapoint["value"] for datapoint in coin["datapoints"][-100:]]

coin_data = sorted(coin_data, key=lambda x: x["exchange"])

st.dataframe(
    coin_data, 
    column_config={
        "image_b64": st.column_config.ImageColumn("Image", width="small"),
        "name": "Symbol",
        "full_name": "Name",
        "asset_id": "Asset ID",
        "exchange": st.column_config.NumberColumn("Exchange Rate (USD)", format="$ %.7f"),
        "trend": st.column_config.AreaChartColumn("Trend", width="medium")
    },
    column_order=("image_b64", "name", "full_name", "asset_id", "exchange", "trend"),
    height=int(60 * 29.8) # Idk why this works
)
