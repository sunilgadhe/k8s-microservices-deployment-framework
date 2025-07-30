import time
import os
import redis
from flask import Flask

#Code starts here

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
cache = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT))

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'CLICK COUNTER! Refresh to see the count increase!\n\nCLICK COUNT: {}\n'.format(count)
