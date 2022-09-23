from turtle import Turtle,Screen
import random
morrocoy = Turtle()
morrocoy.shape("turtle")
morrocoy.color("DarkSeaGreen")

 # for _ in range(4):
 #     morrocoy.forward(100)
 #     morrocoy.right(90)

# for _ in range(20):
#     morrocoy.forward(10)
#     morrocoy.penup()
#     morrocoy.forward(10)
#     morrocoy.pendown()
screen = Screen()
# for _ in range(4):
#     morrocoy.forward(100)
#     morrocoy.right(90)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#
# for _ in range(5):
#     morrocoy.forward(100)
#     morrocoy.right(72)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# for _ in range(6):
#     morrocoy.forward(100)
#     morrocoy.right(60)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# for _ in range(7):
#     morrocoy.forward(100)
#     morrocoy.right(51.4)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# for _ in range(8):
#     morrocoy.forward(100)
#     morrocoy.right(45)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# for _ in range(9):
#     morrocoy.forward(100)
#     morrocoy.right(40)
#
# screen.colormode(255)
# morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# for _ in range(10):
#     morrocoy.forward(100)
#     morrocoy.right(36)

screen.colormode(255)


# def draw_shape(num_sides):
#     angles = 360 / num_sides
#     for _ in range(num_sides):
#         morrocoy.forward(100)
#         morrocoy.right(angles)
#
# for shape_side in range(3,11):
#     draw_shape(shape_side)
#     screen.colormode(255)
    # morrocoy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


def random_walk(num_walks):
    direccion = [0,90,180,270]
    psize=18
    tspeed=10
    for _ in range(num_walks):
        morrocoy.pensize(psize)
        morrocoy.forward(25)
        morrocoy.setheading(random.choice(direccion))
        morrocoy.pencolor(random_color())
        morrocoy.speed(tspeed)
        tspeed -= 1

current_heading = morrocoy.heading()

def spirograph(size_of_gap):
    morrocoy.speed(0)
    morrocoy.pensize(20)
    for circle in range(int(360/size_of_gap)):
        morrocoy.circle(100)
        morrocoy.pencolor(random_color())
        morrocoy.setheading(morrocoy.heading() + size_of_gap)



spirograph(8)
screen.exitonclick()