from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
snake = Snake(screen)
food = Food()
score = Scoreboard()
score.write_text()
game_over = False


while not game_over:

    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        screen.update()
        score.delete_text()
        score.write_text()
        continue
    if snake.head.xcor() > 270 or  snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -270:
        score.game_over()
        game_over = True
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            score.game_over()
            game_over = True
    screen.update()
    time.sleep(0.08)

screen.exitonclick()