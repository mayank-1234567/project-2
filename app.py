import streamlit as st

from config.config import Config
from core.database import DatabaseManager
from services.profile_service import ProfileService
from ui.profile_page import first_time_setup

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon="🚀",
    layout="wide"
)

db = DatabaseManager()
db.initialize_database()

profile = ProfileService()

if not profile.profile_exists():

    first_time_setup()

else:

    user = profile.get_profile()

    st.title(f"👋 Welcome {user[1]}")

    st.success("Profile Loaded Successfully")

    st.write("Dashboard coming in the next phase.")