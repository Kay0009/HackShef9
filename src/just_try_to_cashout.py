import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import database

users = database.get_client()["users"]

# Function to get user balance
def get_user_balance(username):
    user = users.find_one({"username": username})
    if user:
        return user["balance"]
    else:
        return None

# Function to update user balance
def update_user_balance(username, amount):
    users.update_one({"username": username}, {"$inc": {"balance": -amount}})

# Streamlit cashout form
st.title("Cashout")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
        st.write(f"Hello, {username}!")
        st.write(f"Your balance is: ${balance:.2f} USD")

        # Form to cash out
        st.subheader("Cash Out")
        amount = st.number_input("Amount to cash out", min_value=0.0, step=0.01)
        st.write("Transaction fee: 5%")
        st.write("App fee: 5%")
        st.write("Annoyance fee: 6%")
        if st.button("Cash Out"):
            transaction_fee = amount * 0.05
            app_fee = amount * 0.05
            annoyance_fee = amount * 0.06
            total_fees = transaction_fee + app_fee + annoyance_fee
            total_amount = amount + total_fees

            if amount <= balance:
                update_user_balance(username, total_amount)
                st.success(f"${amount:.2f} cashed out. Total fees: ${total_fees:.2f}. Total deducted: ${total_amount:.2f}.")
                st.rerun()
            else:
                st.error("Insufficient balance.")
    else:
        st.error("User not found.")

    # Logout button
    if st.button("Logout"):
        del st.session_state["username"]
        st.rerun()
else:
    st.error("You need to login first.")
