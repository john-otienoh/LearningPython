from turtle import Turtle, Screen
from random import random

my_turtle = Turtle()
my_screen = Screen()

my_turtle.speed('fastest')
#my_screen.colormode(255)

my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for i in range(1, 101):
    my_turtle.color(random(), random(), random())
    my_turtle.dot(20)
    my_turtle.forward(30)
    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(30)
        my_turtle.setheading(180)
        my_turtle.forward(300)
        my_turtle.setheading(0)

my_screen.exitonclick()