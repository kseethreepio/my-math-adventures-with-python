from turtle import *

shape('turtle')
speed(0)

def square(size):
    for i in range(4):
        forward(size)
        right(90)

for i in range(72):
    square(50)
    right(5)

for i in range(36):
    square(80)
    right(10)
