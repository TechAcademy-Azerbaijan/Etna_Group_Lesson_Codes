from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from ..app import app
from ..config.base import Config

app.config.from_object(Config)

login_manager = LoginManager(app)
db = MongoEngine(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
