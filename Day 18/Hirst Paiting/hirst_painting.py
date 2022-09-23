import random

from main import color_list
from turtle import Turtle,Screen

dot = Turtle()
screen = Screen()
screen.colormode(255)
dot.shape("circle")
dot.speed(0)
dot.setheading(0)
current_position = dot.position()
dot.pensize(20)



def horizontal_paint(number_of_dots):
    dot.penup()
    dot.hideturtle()
    dot.setheading(225)
    dot.forward(300)
    dot.setheading(0)


    for dot_count in range(1, number_of_dots + 1):
        dot.dot(20, random.choice(color_list))
        dot.forward(50)

        if dot_count % 10 == 0:
            dot.setheading(90)
            dot.forward(50)
            dot.setheading(180)
            dot.forward(500)
            dot.setheading(0)


horizontal_paint(200)


print(dot.position())






screen.exitonclick()



#def hirst_lines():
