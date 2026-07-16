import streamlit as st

from config.config import Config
from core.database import DatabaseManager
from services.profile_service import ProfileService

from ui.profile_page import first_time_setup
from ui.dashboard import show_dashboard

st.set_page_config(

    page_title=Config.APP_NAME,

    page_icon="🚀",

    layout="wide"

)

db = DatabaseManager()

db.initialize_database()

profile = ProfileService()

if profile.profile_exists():

    user = profile.get_profile()

    show_dashboard(user)

else:

    first_time_setup()