from pymongo import MongoClient
from config.settings import get_settings
from datetime import datetime

settings = get_settings()
client = MongoClient(settings.MONGODB_URI)
db = client.attendance_system

def save_attendance_records(records):
    """Save batch of attendance records to MongoDB"""
    if records:
        return db.attendance.insert_many(records)

def get_attendance_history(filters=None):
    """Get attendance history with optional filters"""
    return list(db.attendance.find(filters or {}))