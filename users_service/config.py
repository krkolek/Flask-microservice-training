"""Base configuration file for the application."""


from os import getenv


APP_PREFIX = 'USERS'


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGO_DBNAME = 'users_db_dev'


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    MONGO_DBNAME = 'users_db_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    MONGO_DBNAME = 'users_db_prod'


CONFIG = {
        'default': DevelopmentConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
}


def get_config():
    """Returns class with appropriate settings"""
    conf = getenv(APP_PREFIX + '_CONFIG', 'default')
    return CONFIG[conf]
