import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Person(object):
    
    Counter = 0
    
    def __init__(self, inheritance = 0.0):  
        Person.Counter += 1
        self.id = Person.Counter        
        self.age = 0
        self.alive = True        
        self.assets = inheritance
              
    @property
    def data(self):
        return {'id': self.id, 'age': self.age, 'assets': self.assets, 'alive': self.alive}
             
    def output(self):
        print str(self.data)

    def earn(self):
        amt = random.randint(1,10)
        self.assets += amt
        
    def consume(self):
        amt = random.randint(1,10)
        self.assets -= amt
        
    def survive(self):
        if self.assets < 0:
            self.alive = False
            
    def live(self):
        if self.alive:
            self.earn()
            self.consume()
            self.survive()
            #self.output()
            self.age += 1
            
    def __str__(self):
        return "Person Object: " + str(self.data) + "\n"
    
df = pd.DataFrame()
people = []
for i in range(1000):
    people.append(Person(inheritance = 1.0))
    df = df.append(people[-1].data, ignore_index=True)
    
for person in people:
    while person.alive and person.age < 10:
        person.live()
        df = df.append(person.data, ignore_index=True)
df.sort_values(by = ["id", "age"], inplace=True)

df['died'] = ((df['alive'].shift(-1) == 0) & (df['id'].shift(-1) == df['id'])).astype(np.int)
df = df.loc[df['alive']==1]

df['died'].unique()
df['died'].value_counts()
sns.countplot(x='died', data=df)

df.groupby('died')['assets'].mean()
df.groupby('age')['died'].mean()



#df['delta'] = df['assets'] - df['assets'].shift(1).fillna(0)
#    
#df.plot(x="age", y=["assets", "delta"], kind = "line")
#plt.axhline(y=0, color='black')
#plt.show()

#person.output()
#person.earn()
#person.consume()
#person.survive()