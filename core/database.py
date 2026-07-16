"""
Database Manager
"""

import sqlite3

from config.config import Config


class DatabaseManager:

    def __init__(self):
        Config.initialize_directories()
        self.db_path = Config.DATABASE_FILE

    def connect(self):
        return sqlite3.connect(self.db_path)

    def initialize_database(self):

        with self.connect() as conn:

            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profile(

                id INTEGER PRIMARY KEY,

                name TEXT,

                age INTEGER,

                occupation TEXT,

                organization TEXT,

                wake_time TEXT,

                sleep_time TEXT,

                productivity_period TEXT,

                timezone TEXT

            )
            """)

            conn.commit()