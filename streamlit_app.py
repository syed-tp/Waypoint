import streamlit as st

st.set_page_config(
    page_title="Waypoint",
    page_icon="static/favicon.png",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        background-image:
            radial-gradient(circle at top, rgba(99, 102, 241, 0.1), transparent 45%),
            linear-gradient(rgba(0, 0, 0, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 0, 0, 0.04) 1px, transparent 1px);
        background-size:
            100% 100%,
            28px 28px,
            28px 28px;
        background-attachment: fixed;
    }
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #ffffff !important;
        background-image: none !important;
    }
    /* Minimal-radius button with padding */
    button[kind="primary"] {
        border-radius: 8px !important;
        padding: 0.55rem 2rem !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container(horizontal=True):
    st.image("static/logo.png", width=280)

st.markdown(
    """
    <div style="font-family: 'Space Grotesk', sans-serif; text-align: center; font-size: 3.7rem; font-weight: 900; color: #111827; -webkit-text-stroke: 1.8px #111827; letter-spacing: 0.02em; margin: 2rem 0; line-height: 1.5;">Structure Long-Form Videos<br>with <span style="background: linear-gradient(#6366f1, #6366f1); background-size: 100% 7px; background-repeat: no-repeat; background-position: 0 95%;">Artificial Intelligence</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Input card
with st.container(horizontal_alignment="center"):
    with st.container(border=True):
        url = st.text_input(
            "Transcript file URL",
            placeholder="https://www.youtube.com/watch?v=...",
            label_visibility="visible",
        )
        with st.container(horizontal_alignment="center"):
            st.button("Generate chapters", type="primary", key="generate_btn")
