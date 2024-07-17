import redis

# Connect to Redis Client
hostname = 'redis-17717.c264.ap-south-1-1.ec2.redns.redis-cloud.com'
portnumber = 17717
password = 'aVM34EdTiZHjNCqsGlQrtj0wDI0ea7ll'

r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)
