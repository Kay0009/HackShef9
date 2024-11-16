import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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

common.footer()
