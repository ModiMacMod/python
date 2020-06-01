# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:38:17 2020

@author: padra
"""

# Youtuber: Kindson The Genius - Simple Linear Regression Tutorial With Python Pandas, Sklearn, Seaborn, Matplolib

import pandas as pd

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
data.head()
data.tail()

import seaborn as sns
%matplotlib inline

sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales')
sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=7, aspect=0.7, kind='reg')

X = data[['x1']]     #This needs to be a dataset
y = data ['y']            #This needs to be a series

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)

print(X_train.shape)
print(X_test)
print(X_train.shape)
print(X_test)

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(X_train, y_train)
print(linreg.intercept_)
print(linreg.coef_)






from sklearn.linear_model import LogisticRegression


log_reg = LogisticRegression()
log_reg.fit(df[['assets']], df['died'])
print(log_reg.intercept_)
print(log_reg.coef_)





from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()

lin_reg.fit(df[['assets']], df['died'])
print(lin_reg.intercept_)
print(lin_reg.coef_)
