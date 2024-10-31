import redis
from redis.backoff import NoBackoff
from redis.retry import Retry


def get_redis_connection(redis_pool, retries: int = 2):
    return redis.Redis(connection_pool=redis_pool, retry_on_timeout=True,
                       retry=Retry(retries=retries, backoff=NoBackoff(),
                                   supported_errors=(ConnectionError, TimeoutError)))


def configure_redis_pool(host: str, port: int, client_name: str, max_connections: int = 30,
                         cache_enabled: bool = False):
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
