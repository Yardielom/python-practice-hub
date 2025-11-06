from imp import new_module
from turtle import Turtle

class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 0
        self.new_turtle = Turtle()
        self.new_turtle.color("white")
        self.new_turtle.hideturtle()
        self.new_turtle.penup()
        self.new_turtle.goto(0,250)


    def write_text(self):

        self.new_turtle.write(f"Score:   {self.score}", align= "center", font=('Courier', 24, 'bold'))
        self.score += 1

    def game_over(self):
        self.new_turtle.goto(0,0)
        self.new_turtle.write("GAME OVER ! ", align= "center", font=('Courier', 20, 'bold'))

    def delete_text(self):
        self.new_turtle.clear()
