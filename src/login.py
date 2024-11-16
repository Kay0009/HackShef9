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

# Streamlit login form
st.title("Login Form")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        # Check if the user exists and the password matches
        user = users_collection.find_one({"username": username, "password": password})
        if user:
            st.session_state["username"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
    else:
        st.error("Please fill in all fields.")