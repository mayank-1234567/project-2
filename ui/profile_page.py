"""
Profile Page
"""

import streamlit as st

from models.user import User
from services.profile_service import ProfileService


service = ProfileService()


def first_time_setup():

    st.header("👋 Welcome")

    st.write("Let's set up your productivity system.")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=18
    )

    occupation = st.selectbox(

        "Occupation",

        [

            "Student",

            "Working Professional",

            "Other"

        ]

    )

    organization = st.text_input(

        "School / College / Company"

    )

    wake = st.time_input("Wake Time")

    sleep = st.time_input("Sleep Time")

    productivity = st.selectbox(

        "Best Productivity Time",

        [

            "Morning",

            "Afternoon",

            "Night"

        ]

    )

    timezone = st.text_input(

        "Timezone",

        value="Asia/Kolkata"

    )

    if st.button("Save Profile"):

        user = User(

            name,

            age,

            occupation,

            organization,

            str(wake),

            str(sleep),

            productivity,

            timezone

        )

        service.save_profile(user)

        st.success("Profile saved!")

        st.rerun()