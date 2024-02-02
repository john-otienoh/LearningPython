from turtle import Turtle, Screen
from random import choice, random
my_turtle = Turtle()
my_screen = Screen()
directions = [0, 90, 180, 270]
my_turtle.pensize(7)
my_turtle.speed(10)
for _ in range(200):
    my_turtle.pencolor(random(), random(), random())
    my_turtle.forward(20)
    my_turtle.setheading(choice(directions))

my_screen.exitonclick()