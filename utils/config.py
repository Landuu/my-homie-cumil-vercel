from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv()
        self.tw_login = os.getenv('TW_USERNAME')
        self.tw_pass = os.getenv('TW_PASSWORD')
        self.kv_url = os.getenv('KV_REST_API_URL')
        self.kv_token = os.getenv('KV_REST_API_TOKEN')
