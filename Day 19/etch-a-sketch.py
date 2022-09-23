from turtle import Turtle,Screen

tortuga = Turtle()
screen = Screen()


def move_fowards():
    tortuga.forward(10)
def move_backwards():
    tortuga.backward(10)

def head_left():
    new_heading = tortuga.heading() +10
    tortuga.setheading(new_heading)


def head_right():
    new_heading = tortuga.heading() -10
    tortuga.setheading(new_heading)

def reset():
    tortuga.reset()

screen.listen()
screen.onkeypress(key="w",fun=move_fowards)
screen.onkeypress(key="s",fun=move_backwards)
screen.onkeypress(key="a",fun=head_left)
screen.onkeypress(key="d",fun=head_right)
screen.onkey(key="c",fun=reset)
screen.exitonclick()
