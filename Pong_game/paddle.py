from turtle import Turtle, Screen

class Paddle(Turtle):
    paddles_list = []
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.screen = Screen()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.goto(position)
        self.showturtle()
        self.paddles_list.append(self)

    def move_left_paddle_up(self):
        if self.paddles_list[1].ycor() < 250:
            self.paddles_list[1].forward(50)

    def move_left_paddle_down(self):
        if self.paddles_list[1].ycor() > -250:
            self.paddles_list[1].backward(50)

    def move_right_paddle_up(self):
        if self.paddles_list[0].ycor() < 250:
            self.paddles_list[0].forward(50)

    def move_right_paddle_down(self):
        if self.paddles_list[0].ycor() > -250:
            self.paddles_list[0].backward(50)


    def move_paddle(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_right_paddle_up, "Up")
        self.screen.onkeypress(self.move_right_paddle_down, "Down")
        self.screen.onkeypress(self.move_left_paddle_up, "w")
        self.screen.onkeypress(self.move_left_paddle_down, "s")

