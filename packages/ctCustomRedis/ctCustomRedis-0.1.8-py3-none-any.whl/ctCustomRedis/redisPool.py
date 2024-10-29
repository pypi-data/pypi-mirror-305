import redis

from ctCustomRedis.redisConnection import get_redis_connection


def configure_redis_pool(host: str, port: int, client_name: str, max_connections: int, cache_enabled: bool=False):
    redis_pool = None
    if cache_enabled and host and port:
        try:
            redis_pool = redis.ConnectionPool(host=host,
                                              port=port,
                                              client_name=client_name,
                                              max_connections=max_connections
                                              )
            redis_conn = get_redis_connection(redis_pool)
            redis_conn.flushall()  # Remove all the existing data
            return redis_pool
        except Exception:
            return None
    else:
        return redis_pool
