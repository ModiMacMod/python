#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:25:05 2019

@author: ModiMacMod
"""

#for part in tweetList[0]:
#    print(part)
import pandas as pd
import numpy as np
import json


df = pd.DataFrame(data=[tweet.created_at for tweet in tweets], columns=['created_at'])
df['id'] = np.array([tweet.id for tweet in tweets])
df['id_str'] = np.array([tweet.id_str for tweet in tweets])
df['text'] = np.array([tweet.text for tweet in tweets])
df['truncated'] = np.array([tweet.truncated for tweet in tweets])
#   entities is a list and needs it's own table (hashtags, symbols, user_mentions, urls)
df['iso_language_code'] = np.array([tweet.metadata['iso_language_code'] for tweet in tweets])
df['result_type'] = np.array([tweet.metadata['result_type'] for tweet in tweets])
df['source'] = np.array([tweet.source for tweet in tweets])
df['in_reply_to_status_id'] = np.array([tweet.in_reply_to_status_id for tweet in tweets])
df['in_reply_to_status_id_str'] = np.array([tweet.in_reply_to_status_id_str for tweet in tweets])
df['in_reply_to_user_id'] = np.array([tweet.in_reply_to_user_id for tweet in tweets])
df['in_reply_to_user_id_str'] = np.array([tweet.in_reply_to_user_id_str for tweet in tweets])
df['in_reply_to_screen_name'] = np.array([tweet.in_reply_to_screen_name for tweet in tweets])
#   geo not quite sure on the for (type, coordinates)
#   coordinates not quite sure on the for (type, coordinates)
#   place not quite sure on the for 
#       (id, url, place_type, name, fullname, country_code, country, contained_within, bounding_box{type, coordinates}, attribute)
#   contributors is no populated in any instance
#df['contributors'] = np.array([tweet.contributors for tweet in tweets])  
df['is_quote_status'] = np.array([tweet.is_quote_status for tweet in tweets])
df['retweet_count'] = np.array([tweet.retweet_count for tweet in tweets])
df['favorite_count'] = np.array([tweet.favorite_count for tweet in tweets])
df['favorited'] = np.array([tweet.favorited for tweet in tweets])
df['retweeted'] = np.array([tweet.retweeted for tweet in tweets])
df['lang'] = np.array([tweet.lang for tweet in tweets])

#   user details
df['user_id'] = np.array([tweet.user.id or 0 for tweet in tweets])
df['user_id_str'] = np.array([tweet.user.id_str for tweet in tweets])
df['user_name'] = np.array([tweet.user.name for tweet in tweets])
df['user_screen_name'] = np.array([tweet.user.screen_name for tweet in tweets])
df['user_location'] = np.array([tweet.user.location for tweet in tweets])
df['user_description'] = np.array([tweet.user.description for tweet in tweets])
df['user_url'] = np.array([tweet.user.url for tweet in tweets])
#   user.entities seems to be a list of urls
df['user_protected'] = np.array([tweet.user.protected for tweet in tweets])
df['user_followers_count'] = np.array([tweet.user.followers_count for tweet in tweets])
df['user_friends_count'] = np.array([tweet.user.friends_count for tweet in tweets])
df['user_listed_count'] = np.array([tweet.user.listed_count for tweet in tweets])
df['user_created_at'] = np.array([tweet.user.created_at for tweet in tweets])
df['user_favourites_count'] = np.array([tweet.user.favourites_count for tweet in tweets])
df['user_utc_offset'] = np.array([tweet.user.utc_offset for tweet in tweets])
df['user_time_zone'] = np.array([tweet.user.time_zone for tweet in tweets])
df['user_geo_enabled'] = np.array([tweet.user.geo_enabled for tweet in tweets])
df['user_verified'] = np.array([tweet.user.verified for tweet in tweets])
df['user_statuses_count'] = np.array([tweet.user.statuses_count for tweet in tweets])
df['user_lang'] = np.array([tweet.user.lang for tweet in tweets])
df['user_contributors_enabled'] = np.array([tweet.user.contributors_enabled for tweet in tweets])
df['user_is_translator'] = np.array([tweet.user.is_translator for tweet in tweets])
df['user_is_translation_enabled'] = np.array([tweet.user.is_translation_enabled for tweet in tweets])
df['user_profile_background_color'] = np.array([tweet.user.profile_background_color for tweet in tweets])
df['user_profile_background_image_url'] = np.array([tweet.user.profile_background_image_url for tweet in tweets])
df['user_profile_background_image_url_https'] = np.array([tweet.user.profile_background_image_url_https for tweet in tweets])
df['user_profile_background_tile'] = np.array([tweet.user.profile_background_tile for tweet in tweets])
df['user_profile_image_url'] = np.array([tweet.user.profile_image_url for tweet in tweets])
df['user_profile_image_url_https'] = np.array([tweet.user.profile_image_url_https for tweet in tweets])
#df['user_profile_banner_url'] = np.array([tweet.user.profile_banner_url for tweet in tweets])
df['user_profile_link_color'] = np.array([tweet.user.profile_link_color for tweet in tweets])
df['user_profile_sidebar_border_color'] = np.array([tweet.user.profile_sidebar_border_color for tweet in tweets])
df['user_profile_sidebar_fill_color'] = np.array([tweet.user.profile_sidebar_fill_color for tweet in tweets])
df['user_profile_text_color'] = np.array([tweet.user.profile_text_color for tweet in tweets])
df['user_profile_use_background_image'] = np.array([tweet.user.profile_use_background_image for tweet in tweets])
df['user_has_extended_profile'] = np.array([tweet.user.has_extended_profile for tweet in tweets])
df['user_default_profile'] = np.array([tweet.user.default_profile for tweet in tweets])
df['user_default_profile_image'] = np.array([tweet.user.default_profile_image for tweet in tweets])
df['user_following'] = np.array([tweet.user.following for tweet in tweets])
df['user_follow_request_sent'] = np.array([tweet.user.follow_request_sent for tweet in tweets])
df['user_notifications'] = np.array([tweet.user.notifications for tweet in tweets])
df['user_translator_type'] = np.array([tweet.user.translator_type for tweet in tweets])

#if tweet.user != None:
#    df['user_id'] = np.array([tweet.user.id for tweet in tweets])
#else:
#    df['user_id'] = None
        

#hashTags = pd.DataFrame(data=None, columns=['text', 'indices_start', 'indices_end'])
#hashTags = hashTags.append({'text': tweetList[833]['entities']['hashtags'][0]['text'], \
#                            'indices_start': tweetList[833]['entities']['hashtags'][0]['indices'][0], \
#                            'indices_end': tweetList[833]['entities']['hashtags'][0]['indices'][1]} , ignore_index=True)
    

#tweetList[833]['metadata']['iso_language_code']
#tweetList[833]['metadata']['result_type']
#tweetList[833]['metadata'].iso_language_code


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)



