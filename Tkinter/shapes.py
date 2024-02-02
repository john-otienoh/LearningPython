from turtle import Turtle, Screen
from random import random
my_turtle = Turtle()
my_screen = Screen()

for i in range(3, 11):
    my_turtle.pencolor(random(), random(), random())
    for _ in range(i):
        angle = 360 // i
        my_turtle.forward(100)
        my_turtle.right(angle)
my_screen.exitonclick()