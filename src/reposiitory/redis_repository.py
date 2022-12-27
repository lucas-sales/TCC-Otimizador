import redis


class RedisRepository:
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0, password="")
