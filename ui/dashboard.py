"""
Dashboard
"""

import streamlit as st


def show_dashboard(user):

    st.title(f"👋 Welcome, {user[1]}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Today's Tasks",
            "0"
        )

        st.metric(
            "Goals",
            "0"
        )

        st.metric(
            "Habits",
            "0"
        )

    with col2:

        st.metric(
            "Productivity",
            "0%"
        )

        st.metric(
            "Study Hours",
            "0"
        )

        st.metric(
            "Current Streak",
            "0"
        )

    st.divider()

    st.subheader("Today's Schedule")

    st.info(
        "No schedule generated."
    )

    st.subheader("AI Recommendation")

    st.info(
        "Recommendations will appear here."
    )