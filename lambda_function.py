from __future__ import print_function
import os
from twitter import *

def lambda_handler(event, context):
    print("Received event: " + str(event))
    token = os.environ['token']
    token_secret = os.environ['token_secret']
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    to_tweet = event["Body"].replace("+", " ")
    
    t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

    t.statuses.update(
    status=str(to_tweet))

    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message><Body>tweet sent</Body></Message></Response>'
