from turtle import Turtle, Screen
my_turtle = Turtle()
my_screen = Screen()

for _ in range(0, 4):
    my_turtle.forward(100)
    my_turtle.left(90)
my_screen.clearscreen()
for step in range(100):
    for c in ('red', 'blue', 'green'):
        my_turtle.begin_fill()
        my_turtle.color(c)
        my_turtle.fillcolor('yellow')
        my_turtle.forward(step)
        my_turtle.right(30)
        my_turtle.end_fill()
my_screen.clearscreen()
for _ in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
my_screen.exitonclick()