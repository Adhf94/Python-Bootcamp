
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard,Midline
import time

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380,0))
ball = Ball()
score = Scoreboard()
midline = Midline()


screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.move_up)
screen.onkeypress(key="Down",fun=r_paddle.move_down)
screen.onkeypress(key="w",fun=l_paddle.move_up)
screen.onkeypress(key="s",fun=l_paddle.move_down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    midline.write_line()

    ball.move()
    #detect ball colision with walls
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()
    #detect ball collisions with paddles.
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 325 or ball.distance(l_paddle) <= 50 and ball.xcor() <= -325:
        ball.bounce_x()
    #detect if ball misses.
    #Increase scores.
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_increase_score()
    if ball.xcor() < -380:
        score.r_increase_score()
        ball.reset_position()



screen.exitonclick()

