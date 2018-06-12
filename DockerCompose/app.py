import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379) # redis is the hostname of the redis container on the application’s network.
                                             # We use the default port for Redis, 6379

def get_hit_count():
    """Following retry loop attempts the request up to 5 times if the redis service is not available.
    This makes our application more resilient if the Redis service needs to be restarted anytime during the app’s lifetime.
    In a cluster, this also helps handling momentary connection drops between nodes.
    """
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
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)