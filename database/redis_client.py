import redis
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB

def get_redis_client():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
