from turtle import Turtle, Screen
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align='left', font='FONT')

    def score_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='left', font='FONT')
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='left', font='FONT')

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            my_y = random.randint(-250, 250)
            new_car.goto(300, my_y)
            self.all_cars.append(new_car)

    def car_mover(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def car_level(self):
        self.car_speed  += MOVE_INCREMENT

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def turtle_finish(self):
        return True if self.ycor() > FINISH_LINE_Y else False

game_is_on = True
player = Player()
car_manager = CarManager()
scores = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=player.up)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.car_mover()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scores.game_over()

        if player.turtle_finish():
            player.goto(STARTING_POSITION)
            car_manager.car_level()
            scores.score_level()
screen.exitonclick()