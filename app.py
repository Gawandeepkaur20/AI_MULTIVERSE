import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from config import APP_TITLE, PAGE_ICON
from utils import initialize_session

from views.home import render_home
from views.chat import render_chat
from views.image_studio import render_image_studio

# ----------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

initialize_session()

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_personality" not in st.session_state:
    st.session_state.selected_personality = "Ethical Hacker"

# ----------------------------------------------------

if st.session_state.page == "home":

    render_home()

elif st.session_state.page == "chat":

    render_chat(client)

elif st.session_state.page == "image":

    render_image_studio(client)