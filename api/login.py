import sys
sys.path.append('../utils')
from http.server import BaseHTTPRequestHandler
from utils.common import send_response_text, get_query_param
from utils.twitter import create_session


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code = get_query_param(self.path, 'code')
        print(code)
        
        if(code is None or len(code) != 6 or not str.isnumeric(code)):
            send_response_text(self, 'Invalid code')
            return
        
        try:
            create_session(code)
        except:
            send_response_text(self, 'Login failed')

        send_response_text(self, 'Login success')
        return
