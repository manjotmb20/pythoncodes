# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:09:55 2019

@author: MA20020997
"""

import math
import numpy as np
from timeit import default_timer as timer
import datetime

def func(f):
    start=timer()
    for i in range(20):
        f=f+1
        print(f)
    end=timer()
    elapsedtime=end-start
    print(elapsedtime)

f=10
func(f)    