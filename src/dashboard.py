import streamlit as st
import common
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
import database

users = database.get_client()["users"] 

common.header()

# Function to get user balance
def get_user_balance(username):
    user = users.find_one({"username": username})
    if user:
        return user["balance"]
    else:
        return None

# Function to update user balance
def update_user_balance(username, amount):
    users.update_one({"username": username}, {"$inc": {"balance": amount}})

# Streamlit dashboard
st.title("Dashboard")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
        st.write(f"Hello, {username}!")
        st.write(f"Your balance is: ${balance:.2f} USD")

        # Form to add funds
        st.subheader("Add Funds")
        amount = st.number_input("Amount to add", min_value=0.0, step=0.01)
        if st.button("Add Funds"):
            update_user_balance(username, amount)
            st.success(f"${amount:.2f} added to your account.")
            st.rerun()
    else:
        st.error("User not found.")

    # Logout button
    if st.button("Logout"):
        del st.session_state["username"]
        st.rerun()
else:
    st.error("You need to login first.")

common.footer()
