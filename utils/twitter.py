from utils.config import Config
from tweety import Twitter

def create_session(extra = None):
    config = Config()
    tw = Twitter('user')
    tw.start(username=config.tw_login, password=config.tw_pass, extra=extra)
    return tw