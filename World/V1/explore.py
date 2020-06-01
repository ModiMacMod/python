# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:04:36 2020

@author: padra
"""

df.head()
df.groupby('died')['assets'].mean()
df.groupby('age')['died'].mean()
df.groupby('age').mean()
df.groupby('age').count()

df['age_bin'] = np.where(df['age'] == 0, 'Born', '')
df['age_bin'] = np.where(((0 < df['age']) & (df['age'] <= 3 )), 'Middle', df['age_bin'])
df['age_bin'] = np.where(df['age'] > 3, 'Old', df['age_bin'])
df.groupby('age_bin').mean()
df['age_bin'].unique()
df['age_bin'].value_counts()
sns.countplot(x = 'age_bin', data=df)

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

df.age.hist()

dummmies_age = pd.get_dummies(df['age'].astype(int), prefix = 'age')
dummmies_age.loc[:,'age_1':]
df = df.join(dummmies_age.loc[:,'age_0':])


df.groupby(['age'])['died'].mean()


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

