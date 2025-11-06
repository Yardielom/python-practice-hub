from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.y = 200
        self.y_score = 0
        self.x_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, self.y)


    def write_score(self):
        self.goto(0, 200)
        self.write( f"{self.y_score} | {self.x_score}", align= "center", font=('Agency FB', 54, 'bold'))
        self.write_interface()

    def write_interface(self):
        for _ in range(10):
                self.y -= 50
                self.setposition(0, self.y)
                self.write(f"|", align="center", font=('Agency FB', 20, 'bold'))
        self.y = 200



    def update_score(self, result):
        if result == "r" :
            self.y_score += 1
        else:
            self.x_score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ! ", align= "center", font=('Courier', 20, 'bold'))

    def delete_text(self):
        self.clear()