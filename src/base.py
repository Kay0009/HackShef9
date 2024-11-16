import streamlit as st
from streamlit_navigation_bar import st_navbar

class BasePage:
    def __call__(self):
        navbar = st_navbar(["Home", "Dashboard"])
        st.write(navbar)

        self.render()

    def render(self):
        raise NotImplementedError("Implement render()")
