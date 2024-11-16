import streamlit as st

import common

common.header()

st.title("Pump & Dump Partners")
st.subheader("An investment advice bureau that starts with you.")
st.subheader("The most trustworthy investment advice bureau in the world.")

st.header("Ready to Invest?")
st.page_link("dashboard.py", label="Get Started")

st.header("Our Top Picks for Today")
c1, c2, c3 = st.columns(3)
c1.metric("Doge", "100", "-4102")
c2.metric("JeffCoin", "200", "-13002")
c3.metric("Hello Coin", "-1023", "-99920")

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
