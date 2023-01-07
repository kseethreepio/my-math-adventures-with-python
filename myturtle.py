from turtle import *

shape('turtle')
speed(0)

def square():
    for i in range(4):
        forward(75)
        right(90)

for i in range(60):
    square()
    right(5)
