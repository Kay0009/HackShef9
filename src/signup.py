import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
import database

users = database.get_client()["users"]

# Streamlit signup form
st.title("Signup Form")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
balance = st.number_input("Initial Balance", min_value=0.0, step=0.01)

if st.button("Signup"):
    if username and password:
        # Check if the user already exists
        if users.find_one({"username": username}):
            st.error("Username already exists. Please choose a different username.")
        else:
            # Add the new user to the database
            user = {
                "username": username,
                "password": password,
                "balance": balance
            }
            users.insert_one(user)
            st.success("User registered successfully!")
    else:
        st.error("Please fill in all fields.")
