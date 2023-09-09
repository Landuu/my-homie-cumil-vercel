from http.server import BaseHTTPRequestHandler
import os
from dotenv import load_dotenv
from upstash_redis import Redis


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        load_dotenv()
        url = os.getenv("KV_REST_API_URL")
        token = os.getenv("KV_REST_API_TOKEN")
        redis = Redis(url=url, token=token)

        data = redis.get('a')
        print(data)
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, test!'.encode('utf-8'))
        return
