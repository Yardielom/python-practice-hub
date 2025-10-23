from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.segments = []

        self.x = 0
        self.create_snake()
        self.head = self.segments[0]


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def create_snake(self):

        for snake in range(3):
            self.add_segment()

    def add_segment(self):
        new_snake = Turtle("square")
        new_snake.hideturtle()
        new_snake.penup()
        new_snake.color("white")
        new_snake.speed("fastest")
        new_snake.goto(self.x, 0)
        new_snake.showturtle()
        self.x += -20
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment()

    def move_snake(self):
        for segment in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(20)

        self.screen.listen()
        self.screen.onkey(self.move_up, "w")
        self.screen.onkey(self.move_down, "s")
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")
