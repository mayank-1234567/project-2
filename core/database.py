"""
Database Manager
----------------
Creates and manages the SQLite database used by the application.
"""

import sqlite3
from pathlib import Path


class DatabaseManager:
    """Handles database initialization and connections."""

    def __init__(self, db_path="database/productivity.db"):
        self.db_path = Path(db_path)

        # Create the database folder if it doesn't exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self):
        """Return a database connection."""
        return sqlite3.connect(self.db_path)

    def initialize_database(self):
        """Create database tables if they don't exist."""

        with self.connect() as conn:
            cursor = conn.cursor()

            # User Profile
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_profile (
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

        print("✅ Database initialized successfully.")