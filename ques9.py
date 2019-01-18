# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:24:40 2019

@author: MA20020997
"""

class TestIterator():
    def __init__(self):
            self.data = ['MyData']
            self.index = -1
            
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

    def __reversed__(self):
        self.index = -1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

r = TestIterator()
itr=iter(r)

for i in reversed(next(itr)):
    print(i)
