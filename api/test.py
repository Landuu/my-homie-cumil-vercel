import sys
sys.path.append('../utils')
from http.server import BaseHTTPRequestHandler
from utils.db import get_db
from utils.common import get_query_param, send_response_text


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code = get_query_param(self.path, 'code')
        print(code is None)
        redis = get_db()

        send_response_text(self, 'Hllo, test!')
        return
