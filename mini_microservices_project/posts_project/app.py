from flask import Flask
from flask_cors import CORS

app = Flask(__name__, )
API_VERSION = 'v1.0'
CORS(app)

API_PREFIX = f'/api/{API_VERSION}'

from routers import *

if __name__ == '__main__':
    app.run(debug=True, port=5001)
