from turtle import Turtle
import random

COLORS = ["lightblue", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_pos = random.randint(-250, 250)
            new_car.goto(300, random_pos)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
