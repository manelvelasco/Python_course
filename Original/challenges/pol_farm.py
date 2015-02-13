# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/alex/.spyder2/.temp.py
"""

x=[2,3]
def pol_farm(*args):
    return lambda x: sum([b*x**k for k,b in enumerate(args)])

mi_pol=pol_farm(1,2,3,4,5,1,1)
print mi_pol(5)    