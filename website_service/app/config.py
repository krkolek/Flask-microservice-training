"""Base configuration file for the application."""

from os import getenv


APP_PREFIX = 'WEBSITE'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'required-by-flash-messages'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGO_DBNAME = 'website_db_dev'


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    MONGO_DBNAME = 'website_db_test'


class ProductionConfig(BaseConfig):
    MONGO_DBNAME = 'website_db_prod'


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
