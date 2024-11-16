import streamlit as st
import common
import pandas as pd
import database

common.header()

users = database.get_client()["users"]
datapoints_collection = database.get_client()["datapoints"]
investments_collection = database.get_client()["investments"]

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

# Function to get user investments
def get_user_investments(username):
    return list(investments_collection.find({"username": username}))

# Streamlit dashboard
st.title("Dashboard")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
        st.write(f"Hello, {username}!")
        st.write(f"Your balance is: ${balance:.2f} USD")

        # Display user investments
        investments = get_user_investments(username)
        if investments:
            st.subheader("Your Investments")
            for investment in investments:
                coin = investment["coin"]
                amount = investment["amount"]
                invested_value = investment["value"]
                current_value = datapoints_collection.find_one({"coin": coin}, sort=[("timestamp", -1)])["value"]
                current_worth = (amount / invested_value) * current_value
                st.write(f"{coin}: Invested ${amount:.2f} at ${invested_value:.7f} per unit, Current worth: ${current_worth:.2f}")

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