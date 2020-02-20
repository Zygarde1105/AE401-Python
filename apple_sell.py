# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:34:58 2020

@author: Richard_Surface1
"""
q = []
n = 0
m = 0
while True:
    a = int(input('What do you want to do: \n 1.設定 \n 2.進貨 \n 3.出貨 \n 4.營業額統計 \n 5.庫存統計 \n else.離開系統'))
    
    if a == 1:
        b = int(input('how much is one apple?'))
        c = int(input('how much apple in store now?'))
        print(b)
        print(c)
    elif a == 2:
        d = int(input('how many apple do you whant to add?'))
        c +=  d
        print('現在有',c)
    elif a == 3: 
        e = int(input('how many apple do you want to buy?'))
        q.append(e) 
        m = b*e
        c -= e 
        print('you need to pay ',m)
    elif a == 4:
        for i in range(len(q)):
            print(q[i])
        print(sum(q)*b)
    elif a == 5:
        print(c) 
    else:
        break
       