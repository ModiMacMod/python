import random
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns



class Firm(object):
    
    Counter = 0
    
    def __init__(self, seed_capital = 1.0):  
        Firm.Counter += 1
        self.id = Firm.Counter        
        self.age = 0
        self.bankrupt = False        
        self.assets = seed_capital
        self.loans = 0
              
    @property
    def data(self):
        return {'id': self.id, 'age': self.age, 'assets': self.assets, 'loans': self.loans, 'bankrupt': self.bankrupt}
             
    def invest(self):
        self.assets -= self.loans * 1.1
        self.loans = max(-self.assets, random.gauss(0, 1))
        self.assets += self.loans
        
    def produce(self):
        self.assets = self.assets * random.uniform(0, 2) 
        if self.assets < self.loans:
            self.bankrupt = True
            
    def cycle(self):
        if not self.bankrupt:
            self.invest()
            self.produce()
            self.age += 1
            
    def __str__(self):
        return "Person Object: " + str(self.data) + "\n"
    
    
firm1 = Firm()
print(firm1)    
firm1.cycle()
    
    
    
ts = time.time()
df = pd.DataFrame()
firms = []
for i in range(100):
    firms.append(Firm(seed_capital = 1.0))
    df = df.append(firms[-1].data, ignore_index=True)
    
for firm in firms:
    while not firm.bankrupt and firm.age < 10:
        firm.cycle()
        df = df.append(firm.data, ignore_index=True)
df.sort_values(by = ["id", "age"], inplace=True)

print(time.time() - ts)


df['default'] = ((df['bankrupt'].shift(-1) == 1) & (df['id'].shift(-1) == df['id'])).astype(np.int)
df = df.loc[df['bankrupt']==0]

df['default'].unique()
df.groupby('age')['default'].value_counts().unstack()
df.groupby('age')['default'].value_counts().unstack().plot(kind='bar')

df.groupby('age')['default'].value_counts(normalize=True).unstack()
df.groupby('age')['default'].value_counts(normalize=True).unstack().plot(kind='bar')
df.groupby('age')['default'].value_counts(normalize=True).unstack()[1].plot(kind='bar')

df.groupby('age')['default'].value_counts(normalize=True).unstack().reset_index()
df.groupby('age')['default'].value_counts(normalize=True).unstack().reset_index().plot.scatter(x='age', y=1)

df.groupby('assets')['default'].mean().reset_index().plot.scatter(x='default', y='assets')
df.groupby('age')['default'].mean().plot(kind='bar')

