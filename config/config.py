 """
Application Configuration
-------------------------
Stores application-wide settings.
"""

from pathlib import Path


class Config:
    """Global application configuration."""

    # App Information
    APP_NAME = "AI Personal Productivity & Schedule Optimizer"
    VERSION = "0.1.0"

    # Root Directory
    ROOT_DIR = Path(__file__).resolve().parent.parent

    # Database
    DATABASE_DIR = ROOT_DIR / "database"
    DATABASE_FILE = DATABASE_DIR / "productivity.db"

    # Backup Folder
    BACKUP_DIR = ROOT_DIR / "backups"

    # Export Folder
    EXPORT_DIR = ROOT_DIR / "exports"

    # Timezone
    DEFAULT_TIMEZONE = "Asia/Kolkata"

    @classmethod
    def initialize_directories(cls):
        """
        Create required directories.
        """
        cls.DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        cls.BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        cls.EXPORT_DIR.mkdir(parents=True, exist_ok=True)