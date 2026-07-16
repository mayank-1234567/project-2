"""
Activity Repository
-------------------
Handles all database operations related to activities.
"""

from core.database import DatabaseManager
from models.activity import Activity
from repositories.activity_mapper import ActivityMapper


class ActivityRepository:

    def __init__(self):
        self.db = DatabaseManager()

    def create_table(self):
        """Create the activities table if it doesn't exist."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS activities(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                title TEXT,
                description TEXT,
                activity_type TEXT,

                category TEXT,
                subject TEXT,

                priority INTEGER,
                difficulty INTEGER,

                estimated_minutes INTEGER,
                actual_minutes INTEGER,

                start_date TEXT,
                due_date TEXT,

                scheduled_date TEXT,
                scheduled_start TEXT,
                scheduled_end TEXT,

                status TEXT,
                progress REAL,

                goal_id INTEGER,

                recurring INTEGER,
                recurrence_rule TEXT,

                energy_required INTEGER,

                tags TEXT,
                notes TEXT,

                ai_score REAL,

                archived INTEGER

            )
            """)

            conn.commit()

    def add(self, activity: Activity):
        """Insert a new activity."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO activities(

                title,
                description,
                activity_type,
                category,
                subject,
                priority,
                difficulty,
                estimated_minutes,
                actual_minutes,
                start_date,
                due_date,
                scheduled_date,
                scheduled_start,
                scheduled_end,
                status,
                progress,
                goal_id,
                recurring,
                recurrence_rule,
                energy_required,
                tags,
                notes,
                ai_score,
                archived

            )

            VALUES(

                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?

            )

            """, (

                activity.title,
                activity.description,
                activity.activity_type,
                activity.category,
                activity.subject,
                activity.priority,
                activity.difficulty,
                activity.estimated_minutes,
                activity.actual_minutes,
                activity.start_date,
                activity.due_date,
                activity.scheduled_date,
                activity.scheduled_start,
                activity.scheduled_end,
                activity.status,
                activity.progress,
                activity.goal_id,
                int(activity.recurring),
                activity.recurrence_rule,
                activity.energy_required,
                activity.tags,
                activity.notes,
                activity.ai_score,
                int(activity.archived)

            ))

            conn.commit()

    def get_all(self):
        """Return all activities."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM activities ORDER BY id DESC")

            rows = cursor.fetchall()

            return [
                ActivityMapper.from_row(row)
                for row in rows
            ]

    def get_by_id(self, activity_id):
        """Return one activity."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM activities WHERE id=?",
                (activity_id,)
            )

            row = cursor.fetchone()

            return ActivityMapper.from_row(row)

    def update(self, activity: Activity):
        """Update an activity."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute("""
            UPDATE activities

            SET

                title=?,
                description=?,
                activity_type=?,
                category=?,
                subject=?,
                priority=?,
                difficulty=?,
                estimated_minutes=?,
                actual_minutes=?,
                start_date=?,
                due_date=?,
                scheduled_date=?,
                scheduled_start=?,
                scheduled_end=?,
                status=?,
                progress=?,
                goal_id=?,
                recurring=?,
                recurrence_rule=?,
                energy_required=?,
                tags=?,
                notes=?,
                ai_score=?,
                archived=?

            WHERE id=?

            """, (

                activity.title,
                activity.description,
                activity.activity_type,
                activity.category,
                activity.subject,
                activity.priority,
                activity.difficulty,
                activity.estimated_minutes,
                activity.actual_minutes,
                activity.start_date,
                activity.due_date,
                activity.scheduled_date,
                activity.scheduled_start,
                activity.scheduled_end,
                activity.status,
                activity.progress,
                activity.goal_id,
                int(activity.recurring),
                activity.recurrence_rule,
                activity.energy_required,
                activity.tags,
                activity.notes,
                activity.ai_score,
                int(activity.archived),
                activity.id

            ))

            conn.commit()

    def delete(self, activity_id):
        """Delete an activity."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM activities WHERE id=?",
                (activity_id,)
            )

            conn.commit()

    def archive(self, activity_id):
        """Archive an activity."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute(
                "UPDATE activities SET archived=1 WHERE id=?",
                (activity_id,)
            )

            conn.commit()

    def complete(self, activity_id):
        """Mark an activity as completed."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE activities

                SET
                    status='Completed',
                    progress=100

                WHERE id=?
                """,
                (activity_id,)
            )

            conn.commit()

    def search(self, keyword):
        """Search activities by title."""

        with self.db.connect() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM activities
                WHERE title LIKE ?
                ORDER BY priority DESC
                """,
                (f"%{keyword}%",)
            )

            rows = cursor.fetchall()

            return [
                ActivityMapper.from_row(row)
                for row in rows
            ]