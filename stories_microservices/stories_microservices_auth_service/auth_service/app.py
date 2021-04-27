from flask import Flask

app = Flask(__name__)

from .config.extentions import db
from .models import *
from .api.routers import api

app.register_blueprint(api, url_prefix='/api/v1.0/auth')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
