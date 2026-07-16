import streamlit as st

from core.database import DatabaseManager

st.set_page_config(
    page_title="AI Productivity Optimizer",
    page_icon="🚀",
    layout="wide"
)

# Initialize database
db = DatabaseManager()
db.initialize_database()

st.title("🚀 AI Personal Productivity & Schedule Optimizer")

st.success("Database connected successfully!")

st.write("""
Welcome!

The application foundation has been created.

Next step:
➡ First-time user profile setup.
""")