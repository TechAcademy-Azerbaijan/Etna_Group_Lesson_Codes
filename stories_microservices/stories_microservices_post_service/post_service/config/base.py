import os
import redis
from datetime import timedelta


BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)


class Config:
    SECRET_KEY = 'this is private'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'super-secret'
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = REFRESH_EXPIRES
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    JWT_BLACKLIST_ENABLED = True
    DEBUG = False if os.environ.get('DEBUG') else True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    DB_USER = os.environ.get('POSTGRES_USER', 'db_user')
    DB_NAME = os.environ.get('POSTGRES_DB', 'db_name')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD', '123')
    DB_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    DB_PORT = os.environ.get('POSTGRES_PORT', '5432')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:6379/0"


class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @property
    def client(cls):
        return redis.Redis(host=cls.HOST, port=cls.PORT, password=cls.PASSWORD, db=0)