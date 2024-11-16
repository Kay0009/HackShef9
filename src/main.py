import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

pg = st.navigation(
    [
        st.Page("index.py"),
        st.Page("dashboard.py")
    ]
)

pg.run()
