import random
from turtle import Turtle
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Scoreboard):
    def __init__(self):
        super().__init__()
        self.new_list = []
        self.y = random.randint(-240, 270)
        self.new_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(0.8, 2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, self.y)
            self.y = random.randint(-240, 270)
            self.new_list.append(new_car)

    def move_cars(self):
        for car in self.new_list:
            car.forward(self.new_speed)

    def level_up(self):
        self.new_speed += MOVE_INCREMENT





