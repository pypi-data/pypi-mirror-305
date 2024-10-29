import redis
from redis.backoff import NoBackoff
from redis.retry import Retry


def get_redis_connection(redis_pool, retries: int=2):
    return redis.Redis(connection_pool=redis_pool, retry_on_timeout=True,
                       retry=Retry(retries=retries, backoff=NoBackoff(),
                                   supported_errors=(ConnectionError, TimeoutError)))
