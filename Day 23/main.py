import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            turtle.squish_t()
            time.sleep(0.5)
            screen.update()
            score.game_over()
            game_is_on = False

    if turtle.is_at_finish():
        score.increase_score()
        car_manager.new_level()
        turtle.pos_reset()


screen.exitonclick()