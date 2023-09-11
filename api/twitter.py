import sys
sys.path.append('../utils')
from http.server import BaseHTTPRequestHandler
from utils.common import send_response_text
from utils.twitter import create_session
from utils.db import get_login_lock
from tweety import Twitter
from os.path import dirname, abspath, join


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        lock = get_login_lock()
        if(lock):
            send_response_text(self, 'Twitter locked, login to refresh user session')
            return
        
        twitter = None
        try:
            dir = dirname(abspath(__file__))
            path = join(dir, '..', 'u')
            twitter = Twitter(path)
            twitter.connect()
        except:
            send_response_text(self, 'Login failed')
            return
            
        tweets = twitter.get_tweets('2Dgirlenjoyer', replies=False)
        
        filtered = []
        for tweet in tweets:
            if(hasattr('is_retweet') and not tweet.is_retweet):
                filtered.append(tweet)

        for f in filtered:
            print(f)

        send_response_text(self, 'Hllo, twitter!' + len(filtered))
        return
