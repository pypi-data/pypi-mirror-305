from sampleRedis.ctRedis import CtRedis


def init_lib(app, logger):
    app.extensions['ct_redis'] = CtRedis(app.config['REDIS_CACHE'], logger)
