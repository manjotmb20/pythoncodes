# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:27:38 2019

@author: MA20020997
"""

import numpy as np
import pandas as pd
import math

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

def func1(x):
    re=math.log10(x)
    return re

def func2(d):
    re=math.radians(d)
    return re

def sin(d):
    re=math.sin(d)
    return re

def cos(d):
    re=math.cos(d)
    return re

def tan(d):
    re=math.tan(d)
    return re
