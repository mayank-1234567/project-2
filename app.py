import streamlit as st

from config.config import Config
from core.database import DatabaseManager

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon="🚀",
    layout="wide"
)

db = DatabaseManager()
db.initialize_database()

st.title(f"🚀 {Config.APP_NAME}")

st.caption(f"Version {Config.VERSION}")

st.success("Foundation initialized successfully.")

st.write(
    """
Welcome!

This project will become an AI-powered productivity assistant.

Current Progress:

✅ Configuration System

✅ Database

⬜ User Profile

⬜ Task Manager

⬜ Goals

⬜ Habits

⬜ Scheduler

⬜ Analytics

⬜ AI Engine
"""
)