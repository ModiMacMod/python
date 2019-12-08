#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:51:28 2019

@author: ModiMacMod
"""


for tweet in tweets:
    print(tweet.entities['hashtags'])
    

hashTags = pd.DataFrame(data=None, columns=['id', 'retweeted', 'text', 'indices_start', 'indices_end'])
for tweet in tweets:
    if len(tweet.entities['hashtags']) > 0:
        for  hashtag in tweet.entities['hashtags']:
            print(hashtag['text'])
            hashTags = hashTags.append({'id': tweet.id, \
                                        'retweeted': tweet.retweeted, \
                                        'text': hashtag['text'], \
                                        'indices_start': hashtag['indices'][0], \
                                        'indices_end': hashtag['indices'][1]} , ignore_index=True)