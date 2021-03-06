# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:27:40 2020

@author: ModiMacMod
"""
import pandas as pd

class Economy:
    
    worker = []
    history = []
    
    def __init__(self, L, A, K, s, g, n, alpha, depreciation):
        self.L = L
        self.A = A
        self.K = K
        self.s = s
        self.g = g
        self.n = n
        self.alpha = alpha
        self.depreciation = depreciation

        self.savings = None
        self.consumption = None
        
          
    def interval(self):
        self.production = (self.A*self.L)**(1-self.alpha)*(self.K)**self.alpha
        self.savings = self.s * self.production
        self.consumption = (1-self.s) * self.production         
        
        hist = (self.L, self.A, self.K, self.production, self.savings, self.consumption)
        self.history.append(hist)
        
        self.L = self.L *(1+self.n)
        self.A = self.A *(1+self.g)
        self.K = self.savings
        
    def loop(self, periods):
        for i in range(periods):
            self.interval()
            
if __name__ == "__main__":
    e = Economy(L=10, A=10, K=1, s=0.3, g=0.01, n=0.01, alpha=0.3, depreciation=0.05)
    e.loop(10) 
    df = pd.DataFrame(e.history, columns=['L', 'A', 'K' , 'production', 'savings', 'consumption'])
    df['k'] = df['K'] / (df['A'] * df['L'])
    df['c'] = df['consumption'] / (df['A'] * df['L'])
    print(df.head())
#    df['consumption'].plot(legend=True)
#    df['production'].plot(legend=True)
#    df['savings'].plot(legend=True)
    df['k'].plot(legend=True)
    df['c'].plot(legend=True)
            
            
        