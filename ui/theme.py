# ui/theme.py

import streamlit as st


def configure_page():
    st.set_page_config(
        page_title="Waypoint",
        page_icon="static/favicon.png",
        layout="wide",
    )


def load_theme():
    st.markdown(
"""<style>

/* ==========================================================
   Design Tokens
========================================================== */

:root {
    --primary:       #6366F1;
    --primary-hover: #4F46E5;

    --text:   #111827;
    --muted:  #6B7280;
    --border: #E5E7EB;

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
}

/* ==========================================================
   Application Background
========================================================== */

.stApp {
    background-color: #ffffff;

    background-image:
        radial-gradient(
            ellipse 650px 320px at 50% 8%,
            rgba(156,163,175,.06),
            transparent 70%
        ),
        linear-gradient(rgba(0,0,0,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,0,0,.04) 1px, transparent 1px);

    background-size:
        100% 100%,
        24px 24px,
        24px 24px;

    background-attachment: fixed;
}

/* ==========================================================
   Buttons
========================================================== */

button[kind="primary"] {
    background:    var(--primary) !important;
    color:         white !important;
    border:        none !important;
    border-radius: var(--radius-sm) !important;
    padding:       .65rem 1.3rem !important;
    font-weight:   600 !important;
    transition:    all .2s ease;
}

button[kind="primary"]:hover {
    background: var(--primary-hover) !important;
    transform:  translateY(-1px);
}

/* ==========================================================
   Text Input
========================================================== */

[data-testid="stTextInput"] input {
    border-radius: var(--radius-md) !important;
    border:        1px solid var(--border) !important;
    background:    white !important;
    padding:       .75rem 1rem !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: var(--primary) !important;
    box-shadow:   0 0 0 3px rgba(99,102,241,.12) !important;
}

/* ==========================================================
   Composer card (border container)
========================================================== */

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: var(--radius-lg) !important;
    border:        1px solid var(--border) !important;
    background:    white !important;
    box-shadow:
        0 1px 2px  rgba(0,0,0,.04),
        0 10px 30px rgba(0,0,0,.05);
}

/* ==========================================================
   Images
========================================================== */

img {
    user-select: none;
    -webkit-user-drag: none;
}

/* ==========================================================
   Hide Streamlit chrome
========================================================== */

#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { background: transparent; }

</style>""",
        unsafe_allow_html=True,
    )