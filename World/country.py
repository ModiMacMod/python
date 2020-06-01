# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:18:02 2020

@author: padra
"""
from person import Person
from firm import Firm
import pandas as pd
import random

class Economy(object):
    
    def __init__(self, name="Brainania", population = 100, businesses = 5): 
        self.__time = 0
        self.__name = name
        self.__population = population
        self.__businesses = businesses
        self.__people = [] 
        self.__firms = []
        
        for i in range(self.__population):
            amt = random.randint(1, 11)     # random integer from 1 to 10
            self.__people.append(Person(amt))
        for i in range(self.__businesses):
            self.__firms.append(Firm())
        
        print(self.__name + " has a population of " + str(self.__population))
    
    def cycle(self):
        self.__time += 1
        self.updateFirms()
        self.updatePeople()
    
    def updateFirms(self): 
        # clear the market 
        for firm in self.__firms:
            firm.clearShareholders()
        for person in self.__people:
            random.choice(self.__firms).sellSharesTo(person)
        for firm in self.__firms:
            firm.raiseCapital()
            firm.produce()
            firm.payDivident()    
    
    def updatePeople(self):
        alive = []
        for person in self.__people:
            person.live()
            alive.append(person.alive)
        df = pd.DataFrame(alive, columns=['alive'])
        print(df['alive'].value_counts())
    
    def returnDF(self):
        time = []
        id_person = []
        age = []
        assets = []
        alive = []
        for person in self.__people:
            time.append(self.__time)
            id_person.append(person.id)
            age.append(person.age)
            assets.append(person.assets)
            alive.append(person.alive)
        return pd.DataFrame(list(zip(time, id_person, age, assets, alive)),
                            columns=['time', 'id', 'age', 'assets', 'alive'])
    
    @property
    def name(self):
        return self.__name
    
    @property
    def population(self):
        return self.__population
    
    @property
    def time(self):
        return self.__time



if __name__ == "__main__":
    country = Economy()  
    df = country.returnDF()      
    country.cycle()      
    df = df.append(country.returnDF()) 
    country.cycle()
    df = df.append(country.returnDF())  
    country.cycle() 
    df = df.append(country.returnDF())
#    country.cycle()
#    df = df.append(country.returnDF())
#    country.cycle()
#    df = df.append(country.returnDF())
    print(df.groupby(['time'])['alive'].value_counts(normalize=True))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
