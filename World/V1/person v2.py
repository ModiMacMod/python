# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:35:06 2020

@author: ModiMacMod
"""

import random
import pandas as pd


class Person(object):    
    Counter = 0
    
    def __init__(self, assets=0.0): 
        Person.Counter += 1
        self.id = Person.Counter
        self.age = 1
        self.assets = assets
        self.alive = True
        
    def live(self):
        if self.alive:
            self.earn()
            self.consume()    
            self.survive()
             
    def earn(self):
        amt = random.randint(1, 10) # random number from 1 to 10
        self.assets += amt
             
    def consume(self):
        amt = random.randint(1, 11) # random number from 1 to 10        
        self.assets -= amt
            
    def survive(self):
        self.age += 1; 
        if self.age > 4 or self.assets < 0:
            self.alive = False
            
    @property
    def dict(self):
        return {'id': self.id, 'age': self.age, 'assets': self.assets, 'alive': self.alive}
             
    def __str__(self):
        return "Person Object: " + str(self.dict) + "\n"
    
    
    
if __name__ == "__main__":
    person1 = Person(10)
    person1.id
    Person.Counter
    person1.assets
    
    person2 = Person(8)
    person2.id
    person2.Counter
    Person.Counter
    person2.assets
    
    person1.Counter
    person2.Counter
        
    #print(person)
    #person.live()
    
    # Begin life
    people = []
    df = pd.DataFrame()
    for i in range(10):
        people.append(Person(1))
        df = df.append(people[-1].dict, ignore_index=True, sort = False)
        
    # loop each year
    for i in range(4):
        for person in people:
            if person.alive:
                person.live()
                df = df.append(person.dict, ignore_index=True, sort = False)
        
                
                
    print(df.groupby(['age'])['alive'].value_counts())
    
    # Buid a model to predict if you will die in the next time period
    target_df = df[['id', 'age', 'alive']].loc[df['age'] > 1]
    target_df['alive'] = target_df['alive'].map({True: 0, False: 1})
    target_df['age'] = target_df['age'] - 1  
    target_df.rename(columns={'alive': 'died'}, inplace = True)
    dev_df = pd.merge(df, target_df, left_on = ['id', 'age'], right_on = ['id', 'age'], how='left')
    dev_df = dev_df.loc[dev_df['died'].notna()]
    dev_df.drop(columns=['alive'], inplace = True)    
    #    select 
    #        t1.*,
    #        case t2.alive 
    #            when False then 0
    #            else 1
    #        end as died
    #    from df t1
    #    left join df t2
    #        on t1.id = d2.id - 1
    #    where t1.alive = True
    
    
    
    
        