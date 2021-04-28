import os
from datetime import timedelta


BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)


class Config:
    SECRET_KEY = 'this is private'
    JWT_SECRET_KEY = 'super-secret'
    DB_NAME = os.environ.get('MONGO_INITDB_DATABASE', 'db_name')
    DB_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'db_user')
    DB_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', '12345')
    DB_HOST = os.environ.get('MONGO_HOST', '127.0.0.1')
    DB_PORT = os.environ.get('MONGO_PORT', '27017')
    MONGODB_SETTINGS = {
        'host': f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin',
        'connect': True
    }
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = REFRESH_EXPIRES
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    JWT_BLACKLIST_ENABLED = True
    DEBUG = False if os.environ.get('DEBUG') else True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
