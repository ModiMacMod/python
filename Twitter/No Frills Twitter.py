#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:31:07 2019

@author: ModiMacMod
"""

ACCESS_TOKEN = "4462851699-taUPFix8LRPr24OuAZFr4CDaIuK7MORkViLxMyJ"
ACCESS_TOKEN_SECRET = "sd3Tk0KaPEAzUfHBubX4aLiqTpOnyb2JotLkepj53YZWu"
CONSUMER_KEY = "Y30ukwzEU8RoIi0lUqKhSnRac"
CONSUMER_SECRET = "gyfU0GADuALLzO3U4g6bD4Qlhk9hY6Oj0vZIP6aapWS3sLpKrU"
print(ACCESS_TOKEN)
print(ACCESS_TOKEN_SECRET)
print(CONSUMER_KEY)
print(CONSUMER_SECRET)


#Import tweepy classes
#    some smart python coders have created tweepy to make life better for all of us :)
#    you will likely need to install tweepy using pip
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API

#Log into twitter API, so that twitter can monitor what data you are extracting from them
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


query = 'Ulster Bank'        # I want to find tweets with the text 'music' in them.  Doesn't have to be a hashtag
geo = '53.2757867,-7.563768,250km'     #  I only want tweets within a 250km radius of the centre of Ireland
cnt = 1000                              #  Only give me the first 250 tweets

#This is the line that extracts the tweets
#tweets = [tweet for tweet in Cursor(api.search, q = query, geocode = geo).items(cnt)]

tweets = [tweet for tweet in Cursor(api.search, q = query).items(cnt)]

