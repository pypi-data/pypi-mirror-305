from sampleRedis.ctRedis import CtRedis


def init_lib(app, logger, redis_pool):
    app.extensions['ct_redis'] = CtRedis(app.config['REDIS_CACHE'], logger,
                                         redis_pool, app.config['REDIS_CACHE_EXPIRE_TIME'])
