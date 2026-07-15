import streamlit as st

def render_logo():
    with st.container(horizontal=True):
        st.image(
            "static/logo.png",
            width=280,
        )