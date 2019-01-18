# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:49:51 2019

@author: MA20020997
"""

import math

class first:
    def __init__(self,x):
        self.x=x
    def method1(self):
        r=self.x+2
        print(r)

class second(first):
    def __init__(self,x):
        super(second,self).__init__(x)
    def method1(self):
        r=self.x+4
        print(r)
        
class third(first):
    def __init__(self,x):
        super(third,self).__init__(x)
    def method1(self):
        r=self.x+6
        print(r)

class fourth(second,third):
    def __init__(self,x):
        super(fourth,self).__init__(x)    
    def method1(self):
        r=self.x*10
        print(r)
        

emp1=fourth(2)   
emp1.method1()  
print("method resolution order is:  fourth->second->first->third->first")   
    
    