import sys
sys.path.append('../utils')
from http.server import BaseHTTPRequestHandler
from utils.common import send_response_text, get_query_param
from utils.config import Config
from tweety import Twitter
from os.path import dirname, abspath, join


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code = get_query_param(self.path, 'code')
        
        if(code is None or len(code) != 6 or not str.isnumeric(code)):
            send_response_text(self, 'Invalid code')
            return

        try:
            dir = dirname(abspath(__file__))
            path = join(dir, '..', 'u')
            config = Config()
            tw = Twitter(path)
            tw.sign_in(username=config.tw_login, password=config.tw_pass, extra=code)
        except:
            send_response_text(self, 'Login failed')
            return

        send_response_text(self, 'Login success')
        return
