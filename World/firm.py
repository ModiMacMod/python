# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:11:17 2020

@author: padra
"""

from person import Person
import random

class Firm(object):
    
    firm_cnt = 0    
    technology = 1.5
    
    def __init__(self):
        print("I consume therefore I am!")
        Firm.firm_cnt += 1
        self.__firm_id = Firm.firm_cnt
        self.__capital = 0.0
        self.__shares = 0
        self.__owners = []
        
    def clearShareholders(self):
        self.__owners = []
        
    def findBuyers(self, buyers):
        self.__owners = buyers
        print("Number of owners is " +str(len(self.__owners)))
        
    def sellSharesTo(self, buyer):
        self.__owners.append(buyer)
        print("Person " + str(buyer.id) + " is buying firm " + str(self.id))
        
    def raiseCapital(self):
        self.__capital = 0.0
        for person in self.__owners:
            amt = float(int(person.assets))
            self.__capital += amt
            person.invest(amt)
        self.__shares = int(self.__capital)
        print("Total Capital is " + str(self.__capital))  
               
    def produce(self):
        self.__capital = self.__capital*Firm.technology
        print("Total production is " +str(self.__capital))
        
    def payDivident(self):
        total_divident = 0
        for person in self.__owners:
            div = self.__capital * (float(person.shares)/float(self.__shares))
            person.earn(div)
            total_divident += div
        self.__capital -= total_divident
        self.__shares = 0
        
        
    @property
    def id(self):
        return self.__firm_id

    @property
    def capital(self):
        return self.__capital
    
    @property
    def shares(self):
        return self.__shares


if __name__ == "__main__":
    firm = Firm()
    people = []
    for i in range(3):
        rnd = random.randint(1,4)
        people.append(Person(assets=rnd))    
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.findBuyers(people)
    ### Round 1
    print("###############################")
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.raiseCapital()
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.produce()  
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.payDivident()
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    ### Round two
    print("###############################")
    firm.raiseCapital()
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.produce()  
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    firm.payDivident()
    print("Firm capital is " + str(firm.capital))
    print("Firm shares are " + str(firm.shares))
    print("People assets are " + str([people[0].assets, people[1].assets, people[2].assets]))
    print("People assets are " + str([people[0].shares, people[1].shares, people[2].shares]))
    
    
    
    
    
    
    
    
    
    
    
    
    