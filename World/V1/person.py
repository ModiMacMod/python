# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:35:06 2020

@author: padra
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
        print("Person " + str(self.id) + " has inherited " + str(self.assets))
        
    def live(self):
        if self.alive:
            self.earn()
            self.consume()    
            self.aging()
        else:
            print("Person " + str(self.id) + " is dead")
             
    def earn(self):
        amt = random.randint(1, 10) # random number from 1 to 10
        self.assets += amt
        print("Person " + str(self.id) + " earned " + str(amt) + " and now has " + str(self.assets))
             
    def consume(self):
        amt = random.randint(1, 11) # random number from 1 to 10
        print("Person " + str(self.id) + " requires " + str(amt) + " and has assets of " + str(self.assets))
        if amt > self.assets:
            self.assets = 0
            self.alive = False
            print("Person " + str(self.id) + " didn't earn enough to surive")
        else:
            self.assets -= amt
            print("Person " + str(self.id) + " has assets of " + str(self.assets))
            
    def aging(self):
        if not self.alive:
            if self.age > 3:
                print("Person " + str(self.id) + " has died of old age") 
                self.alive = False
            else:  
                print("Person " + str(self.id) + " has turned " + str(self.age) + " years old") 
            self.age += 1; 
        else: 
            print("Person " + str(self.id) + " did not make it to old age")
        
    def returnRow():
        return 


if __name__ == "__main__":
    #person = Person(5)
    #person.live()
    
    # Begin life
    people = []
    p_id = []
    alive = []
    age = []
    assets = []
    df = pd.DataFrame(list(zip(p_id, age, assets,  alive)), columns=['id', 'age', 'assets', 'alive'])
    for i in range(10):
        people.append(Person(1))
        p_id.append(people[i].id)
        alive.append(people[i].alive)
        age.append(people[i].age)
        assets.append(people[i].assets)
     
    df = df.append(pd.DataFrame(list(zip(p_id, age, assets, alive)), columns=['id', 'age', 'assets', 'alive']))

    # loop each year
    for i in range(4):
        p_id = []
        alive = []
        age =[]
        assets = []
        for person in people:
            if person.alive:
                person.live()
                p_id.append(person.id)
                alive.append(person.alive)
                age.append(person.age)  
                assets.append(person.assets)  
        df = df.append(pd.DataFrame(list(zip(p_id, age, assets, alive)), columns=['id', 'age', 'assets', 'alive']))
    
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
    
    
    
    
        