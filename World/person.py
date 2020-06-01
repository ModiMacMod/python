# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:35:06 2020

@author: padra
"""

import random
import pandas as pd

class Person(object):
    
    population = 0
    livedEver = 0
    
    def __init__(self, assets=0.0): 
        print("I think therefore I am!")
        Person.population += 1              # Define population as a class attribute
        Person.livedEver += 1
        self.__id = Person.livedEver       # Define id as private
        self.__age = 1
        self.__assets = float(assets)
        self.__shares = 0
        self.__alive = True
        
    def live(self):
        # earn and spend month. If not enough asset, die!!!
        # self.earn()
        self.spend()    
        self.aging()
        self.status()
             
    def earn(self, amt = -1.0):
        if amt == -1.0:
            amt = random.randint(1, 11) # random number from 1 to 10
        self.__assets += float(amt)
        self.__shares = 0
        print("Person " + str(self.__id) + " earned " + str(amt) + " and now has assets of " + str(self.__assets))
             
    def spend(self):
        amt = random.randint(1, 11) # random number from 1 to 10
        print("Person " + str(self.__id) + " requires " + str(amt) + " and  has assets of " + str(self.__assets))
        if amt > self.__assets:
            print("Person " + str(self.__id) + " didn't earn enough to surive")
            self.__assets = 0
            self.__alive = False
        else:
            self.__assets -= amt
            
    def invest(self, amt):
        if amt <= self.__assets:
            self.__assets -= float(amt)
            self.__shares = int(amt)
        else:
            #Let firm know that person has invalid funds
            print("Insufficient Funds")
            
    def aging(self):
        # age 1 year, if older than 3 years of age die!!
        self.__age += 1;   
        if self.__age > 3:
            print("Person " + str(self.__id) + " is very old") 
            self.__alive = False
            
    def status(self):
        # inform world of your age and assetspers
        if self.__alive == False:
            print("Person " + str(self.__id) + " just died")    
        else:
            print("Person " + str(self.__id) + " is " + str(self.__age) + " with assets of " + str(self.__assets))
            
             
    def think(self):
        print("Here I go again: " + str(self.__id))
           
    @staticmethod    
    def population_cnt():
        print("World population is: " + str(Person.population))
            
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        print("No you don't!!!!")
        #self.__id = new_id
        
    @property
    def alive(self):
        return self.__alive
        
    @property
    def assets(self):
        return self.__assets
        
    @property
    def shares(self):
        return self.__shares
    
    @property
    def age(self):
        return self.__age
        
        
    def __private_method(self):
        print("This is how to define a private method")
        
if __name__ == "__main__": 
    people = []
    alive = []
    for i in range(100):
        people.append(Person(5))
        alive.append(people[i].alive)
     
    df = pd.DataFrame(alive, columns=['alive'])
    df['alive'].value_counts()
    
    alive = []
    for person in people:
        person.live()
        alive.append(person.alive)
    
    df = pd.DataFrame(alive, columns=['alive'])
    df['alive'].value_counts()


    
    
    
    
        