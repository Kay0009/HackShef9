import common, database
import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

coin_metadata = database.fetch_coin_metadata()

st.dataframe(
    coin_metadata, 
    column_config={
        "image_b64": st.column_config.ImageColumn("Image", width="small"),
        "name": "Symbol",
        "full_name": "Name",
        "asset_id": "Asset ID"
    },
    column_order=("image_b64", "name", "full_name", "asset_id"),
    height=int(60 * 29.8) # Idk why this works
)
