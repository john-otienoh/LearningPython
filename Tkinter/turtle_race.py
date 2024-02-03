from turtle import Turtle,Screen
from random import randint

my_screen = Screen()
my_screen.setup(width=500, height=500)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nRed\nBlack\nGreen\nBlue\nBrown\nOrange\nEnter a choice")
turtle_colors = ['red', 'black', 'green', 'blue', 'brown', 'orange']
turtle_position = [-100, -60, -20, 20, 60, 100]
turtle_list = []
is_race_on = False

for i in range(0, 6):
    my_turtle = Turtle(shape='turtle')
    my_turtle.penup()
    my_turtle.goto(x=-230, y=turtle_position[i])
    my_turtle.color(turtle_colors[i])
    turtle_list.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle.lower() == user_bet.lower():
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner.")
        distance = randint(0, 10)
        turtles.forward(distance)

my_screen.exitonclick()