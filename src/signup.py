import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB Atlas
database_uri = "mongodb+srv://freddy:1234@hackshef9.ukauu.mongodb.net/?retryWrites=true&w=majority&appName=HackShef9"
client = MongoClient(database_uri, server_api=ServerApi('1'))

# Access the database and collection
db = client["HackShef9"]
users_collection = db["users"]

# Streamlit signup form
st.title("Signup Form")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
balance = st.number_input("Initial Balance", min_value=0.0, step=0.01)

if st.button("Signup"):
    if username and password:
        # Check if the user already exists
        if users_collection.find_one({"username": username}):
            st.error("Username already exists. Please choose a different username.")
        else:
            # Add the new user to the database
            user = {
                "username": username,
                "password": password,
                "balance": balance
            }
            users_collection.insert_one(user)
            st.success("User registered successfully!")
    else:
        st.error("Please fill in all fields.")