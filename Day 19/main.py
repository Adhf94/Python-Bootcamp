import turtle
from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colors = ["red","orange","yellow","blue","purple","green"]
tortugas = []

def new_turtles(num_of_turtles):
    ys = -125
    for turtle_index in range(0,num_of_turtles):
        new_tortuga= Turtle(shape="turtle")
        new_tortuga.color(colors[turtle_index])
        new_tortuga.penup()
        new_tortuga.goto(-230,ys)
        ys += 50
        tortugas.append(new_tortuga)

if user_bet:
    is_race_on = True
new_turtles(6)
while is_race_on:

   for turtle in tortugas:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"Winner turtle was {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()