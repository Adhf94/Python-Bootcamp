import turtle
from turtle import Screen,Turtle
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
marcador = Turtle()
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_data = data.state.to_list()

print(states_data)
game_is_on = True
points = 0
guesses = []
while game_is_on:

    answer_state = screen.textinput(title=f"Guess the state: {points}/50", prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_data:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states.csv")
        break
    if answer_state in states_data:
        guesses.append(answer_state)
        points += 1
        coordenadas = data[data["state"] == f"{answer_state}"]
        xcor = int(coordenadas["x"])
        ycor = int(coordenadas["y"])
        print(xcor, ycor)
        marcador.hideturtle()
        marcador.speed(0)
        marcador.penup()
        marcador.goto(xcor, ycor)
        marcador.pendown()
        marcador.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))
    if points == 50:
        game_is_on = False


