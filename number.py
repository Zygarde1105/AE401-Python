# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:34:56 2020

@author: Richard_Surface1
"""

import random
a = random.randint(1,3)
b = int(input("what number do you guess?"))
if a != b:
    print("you lose" )
else: 
    print("you win")
