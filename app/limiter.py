import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

RATE_LIMIT = 5
WINDOW = 10  # seconds


def is_allowed(client_id: str):
    key = f"rate:{client_id}"

    current = r.incr(key)

    if current == 1:
        r.expire(key, WINDOW)

    if current > RATE_LIMIT:
        return False

    return True
