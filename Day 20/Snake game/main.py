from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreborad import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=snake.Up)
screen.onkeypress(key="Down", fun=snake.Down)
screen.onkeypress(key="Left", fun=snake.Left)
screen.onkeypress(key="Right", fun=snake.Right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(00.1)

    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()