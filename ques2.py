# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 10:06:13 2019

@author: MA20020997
"""

import time
i=1
try:
    x=input()
    time.sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard interrupt")



try:
    name=input("Enter your name")
    print("Hi " + name)
except NameError:
    print("NameError")

try:
    num=0/0
except ArithmeticError:
    print("ArithmeticError")      