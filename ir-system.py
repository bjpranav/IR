# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:06:59 2019

@author: Pranav Krishna
"""
import re
fname = r"D:\bin\AIT-690\Assignments\IR\cran.all.1400"
#docfile

docs={}
prevPointer=None
topic=None
with open(fname) as f:
    for line in f:
        line=line.replace('\n','')
        index=re.findall(r'.I ([0-9]+)',line)
        #print(line)
        if(prevPointer=='.T'):
            topic=line
        if(prevPointer=='.A'):
            author=line
        if(prevPointer=='.B'):
            publication=line
        if(prevPointer=='.W'):
            text=line

        prevPointer=str(line)
        
    