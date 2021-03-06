import random
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns



class Person(object):
    
    Counter = 0
    
    def __init__(self, inheritance = 0.0):  
        Person.Counter += 1
        self.id = Person.Counter        
        self.age = 0
        self.bankrupt = False        
        self.assets = inheritance
              
    @property
    def data(self):
        return {'id': self.id, 'age': self.age, 'assets': self.assets, 'bankrupt': self.bankrupt}
             
    def earn(self):
        amt = random.randint(1,10)
        self.assets += amt
        
    def consume(self):
        amt = random.randint(1,10)
        self.assets -= amt
        if self.assets < 0:
            self.bankrupt = True
            
    def live(self):
        if not self.bankrupt:
            self.earn()
            self.consume()
            self.age += 1
            
    def __str__(self):
        return "Person Object: " + str(self.data) + "\n"
    
ts = time.time()
df = pd.DataFrame()
people = []
for i in range(100):
    people.append(Person(inheritance = 1.0))
    df = df.append(people[-1].data, ignore_index=True)
    
for person in people:
    while not person.bankrupt and person.age < 10:
        person.live()
        df = df.append(person.data, ignore_index=True)
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

df.groupby('assets')['default'].mean().reset_index().plot.scatter(x='assets', y='default')
df.groupby('age')['default'].mean().plot(kind='bar')

