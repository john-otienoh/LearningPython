from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.setup(700, 700)
my_screen.title("My Snake Game")
my_screen.bgcolor('black')
my_screen.tracer(0)
turtle_position = [0, -20, -40]
turtle_list = []

for i in range(0, 3):
    my_turtle = Turtle(shape='square')
    my_turtle.penup()
    my_turtle.color('white')
    my_turtle.goto(x=turtle_position[i], y=0)
    turtle_list.append(my_turtle)

def up():
    turtle_list[0].setheading(90)

def down():
    turtle_list[0].setheading(270)

def left():
    turtle_list[0].setheading(180)

def right():
    turtle_list[0].setheading(0)

# def clear():
#     my_turtle.clear()
#     my_turtle.penup()
#     my_turtle.home()
#     my_turtle.pendown()

my_screen.listen()
my_screen.onkey(key="Up", fun=up)
my_screen.onkey(key='Down', fun=down)
my_screen.onkey(key='Right', fun=right)
my_screen.onkey(key='Left', fun=left)
#my_screen.onkey(clear, "c")
game_on = True

while game_on:
    my_screen.update()
    time.sleep(0.1)
    for turtles in range(len(turtle_list) - 1, 0, -1):
        if turtle_list[0].xcor() > 320:
            game_on = False
        my_new_x = turtle_list[turtles - 1].xcor()
        my_new_y = turtle_list[turtles - 1].ycor()
        turtle_list[turtles].goto(my_new_x, my_new_y)
    turtle_list[0].forward(10)
my_screen.exitonclick()