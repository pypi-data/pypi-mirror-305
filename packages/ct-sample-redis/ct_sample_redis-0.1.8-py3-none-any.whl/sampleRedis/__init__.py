import logging

from flask import Flask
from redis import ConnectionPool

from sampleRedis.ctRedis import CtRedis


def init_cache(app: Flask, logger: logging.Logger, redis_pool: ConnectionPool) -> None:
    """
    Initializes the CtRedis library and attaches it to the Flask app instance for centralized Redis caching.

    This function sets up a Redis caching extension for the application, allowing cached values to be
    stored and retrieved using the CtRedis client. It adds the CtRedis instance to the app’s extensions
    for easy access throughout the application, configured with caching timeout and pooling settings.

    Parameters:
    -----------
    app : Flask
        The Flask application instance where the Redis extension will be initialized.
    logger : logging.Logger
        The logger instance for logging cache-related information, errors, and debugging.
    redis_pool : ConnectionPool
        The Redis connection pool instance used for managing connections to the Redis server.

    Configuration:
    --------------
    `app.config['REDIS_CACHE']`: bool
        Boolean flag indicating whether Redis caching is enabled.
    `app.config['REDIS_CACHE_EXPIRE_TIME']`: int
        Expiration time for cached data, in seconds.

    Redis Pool Setup:
    -----------------
    Use the `configure_redis_pool` function to create the Redis connection pool before passing it
    into `init_lib`. For example:

    ```python
    from sampleRedis.poolConfig import configure_redis_pool

    redis_pool = configure_redis_pool(
        app.config['CACHE_REDIS_HOST'],        # str, Redis host
        app.config['CACHE_REDIS_PORT'],        # int, Redis port
        app.config['CACHE_CLIENT_NAME'],       # str, client name
        max_connections=30,                    # int, max connections
        cache_url=app.config['REDIS_CACHE']    # bool, Redis cache enabled or not
    )
    ```

    Usage:
    ------
    ```python
    from sampleRedis.ctRedis import CtRedis
    from sampleRedis import init_lib

    # Set up the Redis connection pool
    redis_pool = configure_redis_pool(app.config['CACHE_REDIS_HOST'],
                                      app.config['CACHE_REDIS_PORT'],
                                      app.config['CACHE_CLIENT_NAME'],
                                      30,
                                      app.config['REDIS_CACHE'])

    # Initialize the Redis cache
    init_lib(app, logger, redis_pool)
    redis_db = app.extensions['redis_db']

    # Example usage of Redis caching with the decorator
    @redis_db.cache(template_cache_key='idle_time_value:$idle_time', field='$idle_time', is_global=True)
    def get_idle_time_value(idle_time: str) -> str:
        # function logic here
    ```

    Returns:
    --------
    None
        This function does not return any values. It simply configures and adds the CtRedis instance to the app.
    """
    app.extensions['redis_db'] = CtRedis(app.config['REDIS_CACHE'], logger,
                                         redis_pool, app.config['REDIS_CACHE_EXPIRE_TIME'])
