"""
Habit Board — Streamlit host.

The whole app is a self-contained HTML/CSS/JS page that stores everything in the
browser (localStorage + IndexedDB). To keep that storage working, we serve the
page as a STATIC file (real URL / real origin) and load it in an iframe, rather
than inlining the HTML (which runs in an opaque-origin frame where IndexedDB can
fail).

Static file:  static/habit-board.html  ->  served at  app/static/habit-board.html
(requires  enableStaticServing = true  in .streamlit/config.toml)
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Habit Board", page_icon="🌟", layout="wide")

# Strip Streamlit chrome so the board fills the page.
st.markdown(
    """
    <style>
      .block-container {padding: 0.4rem 0.6rem 0 0.6rem; max-width: 100%;}
      header[data-testid="stHeader"] {background: transparent; height: 0;}
      #MainMenu, footer {visibility: hidden;}
      div[data-testid="stDecoration"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# The app manages its own internal scrolling; give the iframe generous height.
# Served as a static file so it keeps a real origin -> localStorage/IndexedDB work.
components.iframe("app/static/habit-board.html", height=1500, scrolling=True)

st.caption(
    "🌟 Kids' Habit Board — data is saved privately in **this browser** on **this device** "
    "(nothing is uploaded). Use the app's ⚙️ Settings → Export/Import to move data between devices."
)
