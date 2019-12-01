#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:31:07 2019

@author: patrickbarry
"""

ACCESS_TOKEN = "4462851699-taUPFix8LRPr24OuAZFr4CDaIuK7MORkViLxMyJ"
ACCESS_TOKEN_SECRET = "sd3Tk0KaPEAzUfHBubX4aLiqTpOnyb2JotLkepj53YZWu"
CONSUMER_KEY = "Y30ukwzEU8RoIi0lUqKhSnRac"
CONSUMER_SECRET = "gyfU0GADuALLzO3U4g6bD4Qlhk9hY6Oj0vZIP6aapWS3sLpKrU"
print(ACCESS_TOKEN)
print(ACCESS_TOKEN_SECRET)
print(CONSUMER_KEY)
print(CONSUMER_SECRET)

from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API

import pandas as pd
import numpy as np
#import json

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

query = 'bank'
geo = '53.2757867,-7.563768,250km'
cnt = 500

tweets = [tweet for tweet in Cursor(api.search, q = query, geocode = geo).items(cnt)]

tweetList = []
for tweet in tweets:
    tweetList.append(tweet._json)
    
df = pd.DataFrame(data=tweet.created_at)

for part in tweetList[0]:
    print(part)