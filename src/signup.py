import streamlit as st
import database
import os

users = database.get_client()["users"]

# Streamlit signup form
st.title("Sign Up")

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "images", "voyageofgains.jpeg")
st.image(image_path, caption="Gain voyage", use_container_width=True)

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
