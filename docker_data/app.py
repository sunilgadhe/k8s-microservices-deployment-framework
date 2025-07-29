import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return int(cache.get('hits') or 0)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def increment_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/api/clicks', methods=['GET', 'POST'])
def clicks():
    if request.method == 'POST':
        count = increment_hit_count()
    else:
        count = get_hit_count()
    return jsonify({'clicks': count})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
