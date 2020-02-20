# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:48:04 2020

@author: Richard_Surface1
"""

import turtle
canvas = turtle.Screen()
canvas.title("SKR")
canvas.bgcolor('black')
skr = turtle.Turtle()
skr.color('white')
skr.shape('turtle')
b = 0
for i in range(0,100):
    b = b+1
    skr.pendown()
    skr.stamp()
    skr.penup()
    skr.forward(20+b)
    skr.left(30)
turtle.done()