import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import database

# Streamlit login form
st.title("Log In")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
st.page_link("signup.py", label="No Account? Get Started")

if st.button("Login"):
    if username and password:
        # Check if the user exists and the password matches
        user = database.get_client()["users"].find_one({"username": username, "password": password})
        if user:
            st.session_state["username"] = username
            st.rerun()
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
    else:
        st.error("Please fill in all fields.")
