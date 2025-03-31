# config.py

import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "shaad"),
    "database": os.getenv("DB_NAME", "srm_faculty_db")
}
