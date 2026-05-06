import json
from app.cache.redis_client import redis_client

CACHE_PREFIX = "request:"
TTL = 60


def get_from_cache(key: str):
    data = redis_client.get(CACHE_PREFIX + key)
    if data:
        return json.loads(data)
    return None


def set_to_cache(key: str, value):
    redis_client.set(
        CACHE_PREFIX + key,
        json.dumps(value),
        ex=TTL
    )


def delete_from_cache(key: str):
    redis_client.delete(CACHE_PREFIX + key)
