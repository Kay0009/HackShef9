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

# Function to add an investment
def add_investment(username, coin, amount, value):
    investment = {
        "username": username,
        "coin": coin,
        "amount": amount,
        "value": value,
        "timestamp": pd.Timestamp.now()
    }
    investments_collection.insert_one(investment)

# Streamlit investment page
st.title("Invest in a Coin")

if "username" in st.session_state:
    username = st.session_state["username"]
    balance = get_user_balance(username)

    if balance is not None:
        st.write(f"Your balance is: ${balance:.2f} USD")

        # Form to invest in a coin
        st.subheader("Invest in a Coin")
        coins = datapoints_collection.distinct("coin")
        selected_coin = st.selectbox("Select a coin", coins)
        coin_value = datapoints_collection.find_one({"coin": selected_coin}, sort=[("time", -1)])["value"]
        st.write(f"Current value of {selected_coin}: ${coin_value:.7f} USD")
        invest_amount = st.number_input("Amount to invest", min_value=0.0, step=10.0)
        if st.button("Invest"):
            if invest_amount <= balance:
                update_user_balance(username, -invest_amount)
                add_investment(username, selected_coin, invest_amount, coin_value)
                st.success(f"Invested ${invest_amount:.2f} in {selected_coin} at ${coin_value:.7f} per unit.")
                st.rerun()
            else:
                st.error("Insufficient balance.")
    else:
        st.error("User not found.")
else:
    st.error("You need to login first.")