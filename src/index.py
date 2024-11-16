import streamlit as st
import database

import common

common.header()

st.title("Pump & Dump Partners")
st.subheader("An investment advice bureau that starts with you.")
st.subheader("The most trustworthy investment advice bureau in the world.")

st.header("Ready to Invest?")
st.page_link("dashboard.py", label="Get Started")

top_picks = (sorted(database.fetch_joined_coin_datapoints(), key=lambda x:float(x["24hr_change"]))[:3])

st.header("Our Top Picks for Today")
c1, c2, c3 = st.columns(3, gap="large")
c1.metric(top_picks[0]["name"], f"${top_picks[0]["datapoints"][-1]["value"]}", f"{float(top_picks[0]["24hr_change"]): .2f}%")
c2.metric(top_picks[1]["name"], f"${top_picks[1]["datapoints"][-1]["value"]}", f"{float(top_picks[1]["24hr_change"]): .2f}%")
c3.metric(top_picks[2]["name"], f"${top_picks[2]["datapoints"][-1]["value"]}", f"{float(top_picks[2]["24hr_change"]): .2f}%")


st.header("Our Values")
st.write("At Pump & Dump Partners, we believe that every investment should start and end with you.")

st.header("Our Reviews")
st.write("Karen - 69 years old")
st.write("I invested my life savings in JeffCoin and now I'm broke. Thanks Pump & Dump Partners!")
st.write("John - 42 years old")
st.write("I invested my life savings in Doge and now I'm broke. Thanks Pump & Dump Partners!")
st.write("Jane - 35 years old")
st.write("I invested my life savings in Hello Coin and now I'm broke. Thanks Pump & Dump Partners!")

common.footer()