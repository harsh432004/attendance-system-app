from database.mongodb import save_attendance_records
from database.redis_client import get_attendance_logs, clear_attendance_logs
from datetime import datetime

def sync_redis_to_mongo():
    """Sync attendance logs from Redis to MongoDB"""
    # Get logs from Redis
    logs = get_attendance_logs()
    
    # Process logs
    attendance_records = []
    for log in logs:
        name, role, timestamp = log.split('@')
        record = {
            'name': name,
            'role': role,
            'timestamp': datetime.fromisoformat(timestamp),
            'synced_at': datetime.utcnow()
        }
        attendance_records.append(record)
    
    # Save to MongoDB and clear Redis
    if attendance_records:
        save_attendance_records(attendance_records)
        clear_attendance_logs()
        
    return len(attendance_records)