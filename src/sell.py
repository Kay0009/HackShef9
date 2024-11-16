import streamlit as st
import pandas as pd
import database

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

# Function to remove an investment
def remove_investment(investment_id):
    investments_collection.delete_one({"_id": investment_id})

# Streamlit selling page
st.title("Sell Your Investments")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
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
                st.write(f"{coin}: Invested ${amount:.2f} at ${invested_value:.2f} per unit, Current worth: ${current_worth:.2f}")
                if st.button(f"Sell {coin}"):
                    update_user_balance(username, current_worth)
                    remove_investment(investment["_id"])
                    st.success(f"Sold {coin} for ${current_worth:.2f}.")
                    st.rerun()
    else:
        st.error("User not found.")
else:
    st.error("You need to login first.")