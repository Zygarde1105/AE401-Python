# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:07:48 2020

@author: Richard_Surface1
"""

n = int(input("what number"))
while True:
    print(n)
    if n ==1:
        break
    if n % 2 ==1:
        n = n*3+1
    else:
        n = n/2
    