"""
Challenge Solution: Reliable Student Management System
Week Five — Session Three
"""

import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
FILE = "reliable_students.json"

def load_roster():
    if not Path(FILE).exists():
        logging.info("No existing roster file found. Starting fresh.")
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to read JSON: {e}")
        return []

roster = load_roster()
logging.info(f"Loaded {len(roster)} students successfully.")
