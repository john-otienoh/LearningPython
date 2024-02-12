from turtle import Turtle, Screen 
import time

my_screen = Screen()
my_screen.setup(800, 600)
my_screen.title("Ping Pong Game")
my_screen.bgcolor('black')
my_screen.tracer(0)

class Players(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.xcord = x
        self.ycord = y
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(self.xcord, self.ycord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = 3
        self.ball_speed = 0.1

    def move(self):
        new_y = self.xcor() + self.x_move
        new_x = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    
    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
    

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1_score, align='center', font=("Arial", 30, "normal"))
        self.goto(100, 200)
        self.write(self.player2_score, align='center', font=("Arial", 30, "normal"))

    def player1_score(self):
        self.player1_score += 1
        self.update_score()

    def player2_score(self):
        self.player2_score += 1
        self.update_score()

player1 = Players(370, 0)
player2 = Players(-370, 0)
ball = Ball()
players_score = ScoreBoard()
game_is_on = True

my_screen.listen()
my_screen.onkey(key='Up', fun=player1.up)
my_screen.onkey(key='Down', fun=player1.down)
my_screen.onkey(key='w', fun=player2.up)
my_screen.onkey(key='s', fun=player2.down)

while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        players_score.player2_score()
    
    if ball.xcor() < -380:
        ball.reset()
        players_score.player1_score()


my_screen.exitonclick()