import redis

# Setup and Connect to Redis Client
# visit website: https://cloud.redis.io and create a redis connection and add hostname and portnumber and password
hostname = 'your redis connection string'
portnumber = "port_number"
password = 'Your redis password'

r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)
