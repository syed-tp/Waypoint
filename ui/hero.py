# ui/hero.py

import streamlit as st

HERO_CSS = """
<style>

@keyframes drawUnderline {
    from {
        transform: scaleX(0);
    }
    to {
        transform: scaleX(1);
    }
}

.hero {
    margin: 2rem auto;
    text-align: center;
}

.hero-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 3.7rem;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -0.02em;
    color: var(--text);
    margin: 0;
}

.ai-underline {
    position: relative;
    display: inline-block;
}

.ai-underline::after {
    content: "";
    position: absolute;

    left: 0;
    right: 0;
    bottom: -2px;

    height: 5px;

    background: var(--primary);
    border-radius: 999px;

    transform: scaleX(0);
    transform-origin: left center;

    animation: drawUnderline .9s cubic-bezier(.22,1,.36,1) forwards;
    animation-delay: .3s;
}

.hero .hero-subtitle {
    max-width: 760px;
    margin: 1.5rem auto 0;

    text-align: center !important;

    color: var(--muted);

    font-size: 1.1rem;
    line-height: 1.7;
    font-weight: 400;
}

</style>
"""

HERO_HTML = """
<div class="hero">
<h1 class="hero-title">
Structure Long-Form Videos<br>
with <span class="ai-underline">Artificial Intelligence</span>
</h1>
<p class="hero-subtitle">
Analyze transcript files to identify natural topic boundaries,<br>
then generate accurate chapter titles and timestamps automatically.
</p>
</div>
"""



def render_hero():
    st.markdown(HERO_CSS, unsafe_allow_html=True)
    st.markdown(HERO_HTML, unsafe_allow_html=True)