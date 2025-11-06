from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.screen = Screen()

    def move_turtle_up(self):
        self.forward(MOVE_DISTANCE)

    def move_turtle(self):
        self.screen.listen()
        self.screen.onkeyrelease(self.move_turtle_up, "w")

    def new_level(self):
        self.goto(STARTING_POSITION)






