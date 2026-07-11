"""
Custom module with error-safe student tools and JSON storage operations.
Week Five — Python Beginner Roadmap
"""

import json
import csv
from pathlib import Path
from logger_config import log_info, log_error

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
JSON_FILE = DATA_DIR / "students.json"
CSV_FILE = DATA_DIR / "students.csv"


def safe_load_json():
    """Safely loads JSON data, handling missing or corrupted files cleanly."""
    if not JSON_FILE.exists():
        log_info("JSON file missing. Starting fresh roster.")
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            log_info(f"Loaded {len(data)} student records.")
            return data
    except json.JSONDecodeError as e:
        log_error(f"Corrupted JSON detected: {e}. Resetting to empty list.")
        print("⚠️ Warning: Student data file corrupted. Starting fresh roster.")
        return []
    except Exception as e:
        log_error(f"Unexpected file read error: {e}")
        return []


def safe_save_json(roster):
    """Safely saves roster to JSON disk file."""
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(roster, f, indent=4)
        log_info(f"Saved {len(roster)} records to disk.")
        print("✅ Data saved successfully.")
    except Exception as e:
        log_error(f"Failed to save JSON: {e}")
        print("❌ Error saving data to disk.")


def safe_export_csv(roster):
    """Safely exports roster to CSV format."""
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Student ID", "Name", "Age", "Department"])
            for s in roster:
                w.writerow([s["student_id"], s["name"], s["age"], s["department"]])
        log_info("Exported CSV successfully.")
        print(f"✅ Exported {len(roster)} records to {CSV_FILE}")
    except Exception as e:
        log_error(f"CSV export failed: {e}")
        print("❌ Error exporting CSV.")
