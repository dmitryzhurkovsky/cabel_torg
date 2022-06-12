import aioredis

from src.core import settings

redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
