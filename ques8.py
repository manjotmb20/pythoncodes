# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:38:57 2019

@author: MA20020997
"""

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)
for x in f:
    print(x)