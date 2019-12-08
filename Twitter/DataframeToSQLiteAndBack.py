#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:40:24 2019

@author: ModiMacMod
"""
from datetime import datetime
import sqlite3
conn=sqlite3.connect("twitter.db")
cur = conn.cursor()                                 


#Write hashtags table
wildcards = ','.join(['?'] * len(hashTags.columns))              
data = [tuple(x) for x in hashTags.values]

cur.execute("drop table if exists %s" % "hashtags")
 
col_str = '"' + '","'.join(hashTags.columns) + '"'
cur.execute("create table %s (%s)" % ("hashtags", col_str))
 
cur.executemany("insert into %s values(%s)" % ("hashtags", wildcards), data)
 

#Write tweets table

df["created_at_str"] = df["created_at"].apply(lambda x: x.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
df["user_created_at_str"] = df["user_created_at"].apply(lambda x: x.strftime("%d-%b-%Y (%H:%M:%S.%f)"))

list = []
for col in df.columns:
    if col not in ["created_at", "user_created_at"]:
        list.append(col)
list

df2 = df[list]


wildcards = ','.join(['?'] * len(df2.columns))              
data = [tuple(x) for x in df2.values]

cur.execute("drop table if exists %s" % "tweets")
 
col_str = '"' + '","'.join(df2.columns) + '"'
cur.execute("create table %s (%s)" % ("tweets", col_str))
 
cur.executemany("insert into %s values(%s)" % ("tweets", wildcards), data)
 


conn.commit()
conn.close()


#    if col not in ["created_at", "user_listed_count", "user_created_at"]:
#timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
# print('Current Timestamp : ', timestampStr)