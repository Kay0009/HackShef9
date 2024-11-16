import streamlit as st

pg = st.navigation(
    [st.Page("pages/index.py"), st.Page("pages/dashboard.py")],
    position = "hidden"
)

pg.run()
