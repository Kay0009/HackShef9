import streamlit as st
import os

st.set_page_config(
    page_icon="https://static.thenounproject.com/png/103213-512.png"
)

# Set the absolute path to the image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "images", "shibacoin.png")
st.sidebar.image(image_path, "Pump and Dump Partners", use_container_width=True)


pg = st.navigation(
    [
        st.Page("index.py", title="Homepage"),
        st.Page("dashboard.py", title="Dashboard"),
        st.Page("invest.py", title="Invest"),
        st.Page("sell.py", title="Sell"),
        st.Page("markets.py", title="Markets"),
        st.Page("signup.py", title="Sign Up"),
        st.Page("login.py", title="Log In"),
        st.Page("just_try_to_cashout.py", title="Cashout"),
    ]
)

pg.run()
