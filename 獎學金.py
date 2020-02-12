# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:02:48 2020

@author: Richard_Surface1
"""

math = int(input("What is your math's score?"))
eng = int(input("What is your english's score?"))
if math >= 90 and eng >= 90:
    print("有獎學金!")
elif math == 100 or eng == 100:
    print("有獎學金!")
else:
    print("再加油")