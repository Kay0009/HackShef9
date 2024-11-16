import common, database
import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

coin_data = database.fetch_joined_coin_datapoints()

for coin in coin_data:
    coin["exchange"] = coin["datapoints"][-1]["value"]

st.dataframe(
    coin_data, 
    column_config={
        "image_b64": st.column_config.ImageColumn("Image", width="small"),
        "name": "Symbol",
        "full_name": "Name",
        "asset_id": "Asset ID",
        "exchange": st.column_config.NumberColumn("Exchange Rate (USD)", format="$ %.7f")
    },
    column_order=("image_b64", "name", "full_name", "asset_id", "exchange"),
    height=int(60 * 29.8) # Idk why this works
)
