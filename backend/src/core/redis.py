import redis

from src.core import settings

redis = redis.from_url(settings.REDIS_URL, decode_responses=True)
