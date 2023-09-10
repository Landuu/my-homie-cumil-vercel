from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler


def get_query_param(path: str, key: str):
    parsed_url = urlparse(path)
    qs = parse_qs(parsed_url.query)
    value = qs.get(key)
    return value[0] if value is not None else None


def send_response_text(http: BaseHTTPRequestHandler, text: str):
    http.send_response(200)
    http.send_header('Content-type','text/plain')
    http.end_headers()
    http.wfile.write(text.encode('utf-8'))