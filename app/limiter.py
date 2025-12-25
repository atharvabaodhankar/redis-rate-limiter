import redis

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

RATE_LIMIT = 5
WINDOW = 10  # seconds


def check_rate_limit(api_key: str):
    key = f"rate:{api_key}"

    current = r.incr(key)

    if current == 1:
        r.expire(key, WINDOW)

    ttl = r.ttl(key)
    remaining = max(RATE_LIMIT - current, 0)

    allowed = current <= RATE_LIMIT

    return {
        "allowed": allowed,
        "limit": RATE_LIMIT,
        "remaining": remaining,
        "reset": ttl
    }
