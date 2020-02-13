# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:34:56 2020

@author: Richard_Surface1
"""

import random
answer = random.randint(1,10)
t = 0
while t < 5:
    guess = int(input("what number do you guess?"))
    if guess >= 1 and guess <= 10:
        t = t+1
        if answer < guess:
            if t == 5:
                print("sorry, you have been guessing five times")
            else:
                print("guess smaller")
        elif answer > guess:
            if t == 5:
                print("sorry, you have been guessing five times")
            else:
                print("guess bigger")
        else:
            print("good")
            print("you guess ",t," times")
            break
    else:
        print("try again")
    
        
