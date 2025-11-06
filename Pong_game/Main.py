import time
from turtle import Screen
from score import Score
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_paddle.move_paddle()
game_over = False
ball = Ball()
score = Score()
score.write_score()

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and  ball.xcor() > 320 or ball.distance(l_paddle) < 40 and  ball.xcor() < -320:
            ball.bounce_x()

    if ball.xcor() > 370:
        score.update_score("r")
        ball.reset_position()
        score.delete_text()
        score.write_score()
    elif ball.xcor() < -370:
        score.update_score("l")
        ball.reset_position()
        score.delete_text()
        score.write_score()




screen.exitonclick()

