"""
User Model
"""

from dataclasses import dataclass


@dataclass
class User:

    name: str

    age: int | None

    occupation: str

    organization: str

    wake_time: str

    sleep_time: str

    productivity_period: str

    timezone: str
