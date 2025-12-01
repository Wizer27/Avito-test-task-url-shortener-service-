import redis


redis_cli = redis.Redis(host = "0.0.0.0",port = 8081)

def write_data(main_url:str,slug:str) -> bool:
    if redis_cli.exists(slug):
        return False
    redis_cli.set(slug,main_url)

def get_url_by_slug(slug:str) -> str:
    if not redis_cli.exists(slug):
        raise KeyError("Slug not found")
    return str(redis_cli.get(slug))