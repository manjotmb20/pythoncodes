# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:26:04 2019

@author: MA20020997
"""

import math

class sqroot:
    def __init__(self,x,y):
           self.x=x
           self.y=y
    def sq(self):
        r=math.sqrt(self.x)
        print(r)
class addition:
    def __init__(self,x,y):
           self.x=x
           self.y=y
    def add(self):
        r=(self.x)+(self.y) 
        print(r)

class subtraction:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sub(self):
        r=self.x-self.y 
        print(r) 

class multiplication:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mul(self):
        r=self.x*self.y 
        print(r) 

class division:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def div(self):
        r=self.x/self.y 
        print(r) 

class mathnew(sqroot,addition,subtraction,multiplication,division):
    def __init__(self,x,y):
        super(mathnew,self).__init__(x,y)
        

emp=mathnew(2,3)        
emp.add()
emp.sub()
emp.sq()
emp.mul()
emp.div()
