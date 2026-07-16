"""
Activity Mapper
---------------

Converts SQLite rows into Activity objects
and Activity objects into dictionaries.
"""

from models.activity import Activity


class ActivityMapper:

    @staticmethod
    def from_row(row):

        if row is None:
            return None

        return Activity(

            id=row[0],

            title=row[1],

            description=row[2],

            activity_type=row[3],

            category=row[4],

            subject=row[5],

            priority=row[6],

            difficulty=row[7],

            estimated_minutes=row[8],

            actual_minutes=row[9],

            start_date=row[10],

            due_date=row[11],

            scheduled_date=row[12],

            scheduled_start=row[13],

            scheduled_end=row[14],

            status=row[15],

            progress=row[16],

            goal_id=row[17],

            recurring=bool(row[18]),

            recurrence_rule=row[19],

            energy_required=row[20],

            tags=row[21],

            notes=row[22],

            ai_score=row[23],

            archived=bool(row[24])

        )