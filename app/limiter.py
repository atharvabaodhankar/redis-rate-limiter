import redis

r = redis.Redis(
    host="redis",   # docker service name
    port=6379,
    decode_responses=True
)

RATE_LIMIT = 5
WINDOW = 10


def is_allowed(client_id: str):
    key = f"rate:{client_id}"

    current = r.incr(key)

    if current == 1:
        r.expire(key, WINDOW)

    return current <= RATE_LIMIT
