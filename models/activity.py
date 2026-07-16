"""
Activity Model
--------------

Universal model used throughout the application.

Every task, habit, study session,
meeting and reminder is stored as an Activity.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Activity:

    # Unique ID
    id: Optional[int] = None

    # Basic Information
    title: str = ""
    description: str = ""

    # Activity Type
    activity_type: str = "Task"

    # Organization
    category: str = "General"
    subject: str = ""

    # Priority
    priority: int = 3          # 1 - 5
    difficulty: int = 3        # 1 - 5

    # Time
    estimated_minutes: int = 60
    actual_minutes: int = 0

    # Dates
    start_date: str = ""
    due_date: str = ""

    # Schedule
    scheduled_date: str = ""
    scheduled_start: str = ""
    scheduled_end: str = ""

    # Status
    status: str = "Pending"

    # Progress
    progress: float = 0.0

    # Goal Connection
    goal_id: Optional[int] = None

    # Habit
    recurring: bool = False
    recurrence_rule: str = ""

    # Energy
    energy_required: int = 3

    # Tags
    tags: str = ""

    # Notes
    notes: str = ""

    # AI
    ai_score: float = 0.0

    # Archive
    archived: bool = False
