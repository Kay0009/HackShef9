import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

pg = st.navigation(
    [
        st.Page("index.py"),
        st.Page("dashboard.py"),
        st.Page("markets.py"),
        st.Page("signup.py"),
        st.Page("login.py")
    ]
)

pg.run()
