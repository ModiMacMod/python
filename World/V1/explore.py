# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:04:36 2020

@author: padra
"""

df.head()
df.groupby(['age', 'default'])['assets'].mean().unstack()
df.groupby('age')['default'].mean()
df.groupby('age')['assets', 'bankrupt', 'default'].mean()
df.groupby('age')['id'].count()

df['wealth'] = np.where(df['assets'] <= 5, '1. Poor', '')
df['wealth'] = np.where(((5 < df['assets']) & (df['age'] <= 10 )), '2. Middle', df['wealth'])
df['wealth'] = np.where(df['assets'] > 10, '3. Rick', df['wealth'])
df.groupby(['age'])['wealth'].value_counts().unstack()
df.groupby(['age', 'wealth'])['default'].mean().unstack()
df['wealth'].unique()
df['wealth'].value_counts()
df['wealth'].value_counts().plot(kind='bar')
sns.countplot(x = 'age', hue='wealth', data=df)
sns.countplot(x = 'wealth', hue='age', data=df)

count_died = len(df[df['died']==1])
count_total = len(df['id'].unique())
print("Of " + str(count_total) + " people, " + str(count_died) + " died")


#%matplotlib
pd.crosstab(df['age_bin'], df['died'])
pd.crosstab(df['age_bin'], df['died']).plot(kind='bar')
plt.title('This is a title')
plt.xlabel('This is the x-label')
plt.ylabel('This is the y-label')

table = pd.crosstab(df['age_bin'], df['died'])
table.div(table.sum(1).astype(float), axis=0)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)

df['age'].hist()
df['assets'].hist()


dummmies_age = pd.get_dummies(df['age'].astype(int), prefix = 'age')
dummmies_age.loc[:,'age_1':]
df = df.join(dummmies_age.loc[:,'age_0':])


df.groupby(['age'])['died'].mean()
df.plot(kind='scatter', x='age', y='assets')


df.loc[df['assets']<11].groupby(['assets'])['died'].mean().plot()
df.loc[df['assets']<11].groupby(['assets'])['died'].mean()
df.groupby(['age'])['alive'].count().plot()



import statsmodels.api as sm

df['intercept'] = 1
df['assetsSq'] = df['assets'] * df['assets']
log_reg = sm.Logit(df['died'], df[['intercept', 'age_1', 'age_2', 'age_3', 'age_4', 'age_5', 'age_6']])
results = log_reg.fit()
results.summary()
print(results.summary2())


log_reg = sm.Logit(df['died'], df[['intercept', 'age_1', 'age_2', 'age_3', 'age_4', 'age_5', 'age_6', 'assets']])
results = log_reg.fit()
results.summary()

log_reg = sm.Logit(df['died'], df[['intercept', 'age_1', 'age_2', 'age_3', 'age_4', 'age_5', 'age_6', 'assets', 'assetsSq']])
results = log_reg.fit()
results.summary()


lin_reg = sm.OLS(df['assets'], df[['intercept', 'age',]])
results = lin_reg.fit()
results.summary()


