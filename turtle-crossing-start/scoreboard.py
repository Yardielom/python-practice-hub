from turtle import Turtle
FONT = ("Agency FB", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()


    def write_level(self):
        self.goto(-240, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)

    def delete_level(self):
        self.clear()


