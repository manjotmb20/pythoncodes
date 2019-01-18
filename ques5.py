# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:09:37 2019

@author: MA20020997
"""

import re
import fileinput
import sys
patterns='[aeiou][aeiou]'
text= ['abcdeu','ae','re','aji','rabcei']
for line in text:
    if re.search(patterns,line):
        print(line)
    else:
        print('no match')