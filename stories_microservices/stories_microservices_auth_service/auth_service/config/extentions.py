import datetime
import os

import redis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from ..app import app

BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')


class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @property
    def client(self):
        return redis.Redis(host=self.HOST, port=self.PORT, password=self.PASSWORD, db=0)


app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://auth_db_user:123@127.0.0.1:5433/auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['SECRET_KEY'] = 'LSKNDFKLNSDFLKNSDFLK'
app.config['SECURITY_PASSWORD_SALT'] = 'My_Salt'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=30)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
