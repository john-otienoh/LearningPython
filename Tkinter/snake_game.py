from turtle import Turtle, Screen
import time
from random import randint 

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.goto(randint(-330, 330), randint(-330, 330))
        self.refresh()

    def refresh(self):
        self.goto(randint(-330, 330), randint(-330, 330))


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.write(f"Score: {self.score}", align='left', font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='left', font=("Arial", 20, "normal"))
    def scores(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='left', font=("Arial", 20, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"High Score: {self.score}", align='left', font=("Arial", 20, "normal"))

my_screen = Screen()
my_screen.setup(700, 700)
my_screen.title("My Snake Game")
my_screen.bgcolor('black')
my_screen.tracer(0)
turtle_position = [0, -20, -40]
turtle_list = []
up_dir, down_dir, left_dir, right_dir = 90, 270, 180, 0
my_food = Food()
user_scores = ScoreBoard()

for i in range(0, 3):
    my_turtle = Turtle(shape='square')
    my_turtle.penup()
    my_turtle.color('white')
    my_turtle.goto(x=turtle_position[i], y=0)
    turtle_list.append(my_turtle)
    

def up():
    if turtle_list[0].heading() != down_dir:
        turtle_list[0].setheading(90)

def down():
    if turtle_list[0].heading() != up_dir:
        turtle_list[0].setheading(270)

def left():
    if turtle_list[0].heading() != right_dir:
        turtle_list[0].setheading(180)

def right():
    if turtle_list[0].heading() != left_dir:
        turtle_list[0].setheading(0)

my_screen.listen()
my_screen.onkey(key="Up", fun=up)
my_screen.onkey(key='Down', fun=down)
my_screen.onkey(key='Right', fun=right)
my_screen.onkey(key='Left', fun=left)

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    for turtles in range(len(turtle_list) - 1, 0, -1):
        if turtle_list[0].xcor() > 330 or turtle_list[0].xcor() < -330 or turtle_list[0].ycor() > 330 or turtle_list[0].ycor() < -330:
            user_scores.game_over()
            game_on = False
        my_new_x = turtle_list[turtles - 1].xcor()
        my_new_y = turtle_list[turtles - 1].ycor()
        turtle_list[turtles].goto(my_new_x, my_new_y)
    turtle_list[0].forward(10)
    if turtle_list[0].distance(my_food) < 15:
        my_food.refresh()
        # lastposition = turtle_list[-1].position()
        # new_turtle = Turtle(shape='square')
        # turtle_list.append(new_turtle)
        # new_turtle.goto(lastposition)
        user_scores.scores()
    # for s in turtle_list:
    #     if s == turtle_list:
    #         pass
    #     elif turtle_list[s] < 10:
    #         game_on = False
    #         user_scores.game_over()
my_screen.exitonclick()