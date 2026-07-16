"""
Profile Service
"""

from core.database import DatabaseManager
from models.user import User


class ProfileService:

    def __init__(self):

        self.db = DatabaseManager()

    def profile_exists(self):

        conn = self.db.connect()

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM user_profile")

        count = cursor.fetchone()[0]

        conn.close()

        return count > 0

    def save_profile(self, user: User):

        conn = self.db.connect()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO user_profile(

        name,

        age,

        occupation,

        organization,

        wake_time,

        sleep_time,

        productivity_period,

        timezone

        )

        VALUES(?,?,?,?,?,?,?,?)

        """, (

            user.name,

            user.age,

            user.occupation,

            user.organization,

            user.wake_time,

            user.sleep_time,

            user.productivity_period,

            user.timezone

        ))

        conn.commit()

        conn.close()

    def get_profile(self):

        conn = self.db.connect()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user_profile LIMIT 1")

        row = cursor.fetchone()

        conn.close()

        return row