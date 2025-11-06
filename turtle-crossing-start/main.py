import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing 🐢")
turtle = Player()
car_manager = CarManager()
interface = Scoreboard()
game_is_on = True
interface.write_level()

while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    turtle.move_turtle()
    screen.update()
    if turtle.ycor() == 280:
        turtle.new_level()
        interface.level += 1
        car_manager.level_up()
        interface.delete_level()
        interface.write_level()
    for car in car_manager.new_list:
        if turtle.distance(car) < 32:
            interface.write_game_over()
            game_is_on = False


screen.exitonclick()