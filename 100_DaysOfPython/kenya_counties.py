#!/usr/bin/python3
import turtle
import csv

my_screen = turtle.Screen()
my_screen.setup(width=600, height=600)
image = 'kenya.gif'
my_screen.addshape(image)
turtle.shape(image)

counties = list(csv.DictReader(open('county.csv')))
counties_list = [c for c in counties]

guessed_counties = []

user_answer = my_screen.textinput(title=f'{len(guessed_counties)}/ 47 Counties Correct', prompt="What's another County's name").title()
while len(guessed_counties) < 47:
    if user_answer == "Exit":
        missed_counties = [c for c in counties_list if c not in guessed_counties]
        break
    if user_answer in counties_list:
        guessed_counties.append(user_answer)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        #county_cordinates = 
        # my_turtle.goto()
        # my_turtle.write(user_answer)

turtle.mainloop()