import streamlit as st

st.set_page_config(
    page_icon="https://static.thenounproject.com/png/103213-512.png"
)

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
        st.Page("market_graphs.py", title="Market Graphs")
    ]
)

pg.run()
