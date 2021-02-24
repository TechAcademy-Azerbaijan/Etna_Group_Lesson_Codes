from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_client = Redis(host='redis_service', port=6379)

@app.route('/')
def welcome():
    hits = redis_client.incr('hits')
    return f'<h1>Hello World. This page called {hits} times</h1>'
