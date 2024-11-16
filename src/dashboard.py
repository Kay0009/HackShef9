import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

<<<<<<< HEAD
# Load environment variables from .env file
load_dotenv()
=======
import common, database
>>>>>>> c55f1d9 (Dataframe in streamlit)

# Connect to MongoDB Atlas
database_uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"
client = MongoClient(database_uri, server_api=ServerApi('1'))

# Access the database and collection
db = client["HackShef9"]
users_collection = db["users"]


# Function to get user balance
def get_user_balance(username):
    user = users_collection.find_one({"username": username})
    if user:
        return user["balance"]
    else:
        return None


# Streamlit dashboard
st.title("Dashboard")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
        st.write(f"Hello, {username}!")
        st.write(f"Your balance is: ${balance:.2f} USD")
    else:
        st.error("User not found.")

    # Logout button
    if st.button("Logout"):
        del st.session_state["username"]
        st.rerun()
else:
    st.error("You need to login first.")

coin_metadata = database.fetch_coin_metadata()

for coin in coin_metadata:
    coin["image_b64"] = "data:image/png;base64," + coin["image_b64"]

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

common.footer()
