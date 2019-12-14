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

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    max_words = 100,
    background_color = 'white',
    stopwords = stopwords).generate(' '.join(df['text']))

#wordcloud.to_file("img/first_review.png")

fig = plt.figure(
#    figsize = (40, 30),
#    facecolor = 'k',
#    edgecolor = 'k'
    )

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


