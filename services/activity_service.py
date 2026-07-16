"""
Activity Service
----------------

Handles all activity related operations.
"""

from models.activity import Activity


class ActivityService:

    def __init__(self):

        self.activities = []

    def add_activity(self, activity: Activity):

        self.activities.append(activity)

    def get_all(self):

        return self.activities

    def get_pending(self):

        return [

            activity

            for activity in self.activities

            if activity.status == "Pending"

        ]

    def get_completed(self):

        return [

            activity

            for activity in self.activities

            if activity.status == "Completed"

        ]

    def complete(self, activity_id):

        for activity in self.activities:

            if activity.id == activity_id:

                activity.status = "Completed"

                activity.progress = 100

                return True

        return False

    def archive(self, activity_id):

        for activity in self.activities:

            if activity.id == activity_id:

                activity.archived = True

                return True

        return False