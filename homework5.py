# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:36:50 2020

@author: Richard_Surface1
"""
   
nameh = 0
namel = 0
a = [['q',1],['w',2],['e',3],['r',4],['t',5]]
def skr(x):
    total = 0 
    for i in range(len(a)):
        total += a[i][1]
    return total / len(a)    
def skr_skr(x):
    high = -1
    global nameh
    for i in range(len(a)):
        if a[i][1] > high:
            high = a[i][1]
            nameh = i
    return high
def skr_skr_skr(x):
    low = 101
    global namel
    for i in range(len(a)):
        if a[i][1] < low:
            low = a[i][1]
            namel = i
    return low  
print('average:',skr(a))
print('highest:',skr_skr(a),a[nameh][0])
print('lowest:',skr_skr_skr(a),a[namel][0])