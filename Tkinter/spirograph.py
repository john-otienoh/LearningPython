from turtle import Turtle, Screen
from random import random

my_turtle = Turtle()
my_screen = Screen()

my_turtle.speed('fastest')
for _ in range(120):    
    my_turtle.color(random(), random(), random())
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + 10)
my_screen.exitonclick()