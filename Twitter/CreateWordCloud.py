#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:28:33 2019

@author: ModiMacMod
"""

 
import pandas as pd
import numpy as np

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt



# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["https", "co", "flavors"])


df2 = df[['text']]
df2['text'].apply(lambda x: x.encode('utf-8').strip())
df2['retweet'] = df2['text'].str[:2]
df2 = df2[ df2['retweet']!='RT' ]


wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    max_words = 100,
    background_color = 'white',
    stopwords = stopwords).generate(' '.join(df2['text']))
                      
#wordcloud.to_file("img/first_review.png")

fig = plt.figure(
    figsize = (30, 20),
    facecolor = 'k',
    edgecolor = 'k'
    )

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


