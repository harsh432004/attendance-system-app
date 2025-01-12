import redis
from config.settings import get_settings

settings = get_settings()

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    decode_responses=True
)

def save_attendance_log(name, role, timestamp):
    """Save attendance log to Redis"""
    log_data = f"{name}@{role}@{timestamp}"
    return redis_client.lpush('attendance:logs', log_data)

def get_attendance_logs():
    """Get all attendance logs from Redis"""
    return redis_client.lrange('attendance:logs', 0, -1)

def clear_attendance_logs():
    """Clear attendance logs after sync"""
    return redis_client.delete('attendance:logs')