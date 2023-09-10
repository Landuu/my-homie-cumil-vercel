from upstash_redis import Redis
from .config import Config

def get_db():
    config = Config()
    return Redis(url=config.kv_url, token=config.kv_token)


def set_login_lock(state: bool):
    r = get_db()
    r.set('login_lock', state)


def get_login_lock():
    r = get_db()
    state = r.get('login_lock')
    if(state is None):
        return False
    return bool(state)