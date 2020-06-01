# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:35:06 2020

@author: ModiMacMod
"""

class Person(object):    
    Counter = 0
    
    def __init__(self, assets=0.0): 
        Person.Counter += 1
        self.id = Person.Counter
        self.age = 1
        self.assets = assets
        self.alive = True
        
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
        