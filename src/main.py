import streamlit as st
import os

st.set_page_config(
    page_icon="https://static.thenounproject.com/png/103213-512.png"
)

# Set the absolute path to the image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "images", "shibacoin.png")
st.sidebar.image(image_path, "Pump & Dump Partners", use_container_width=True)

base_pages = [
    st.Page("index.py", title="Homepage"),
    st.Page("markets.py", title="Markets"),
    st.Page("signup.py", title="Sign Up"),
    st.Page("login.py", title="Log In")
]

logged_in_pages = [
    st.Page("dashboard.py", title="Dashboard"),
    st.Page("invest.py", title="Invest"),
    st.Page("sell.py", title="Sell"),
    st.Page("just_try_to_cashout.py", title="Cashout")
]

pages = base_pages

if "username" in st.session_state:
    pages[1:1] = logged_in_pages # https://stackoverflow.com/a/7376026

pg = st.navigation(pages)

pg.run()
