from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, randint(-260, 260))
        new_car.move_speed = STARTING_MOVE_DISTANCE
        self.cars.append(new_car)

    def move(self, value):
        for car in self.cars:
            new_x = car.xcor() - car.move_speed
            car.goto(new_x, car.ycor())
        if value % 5 == 0:
            self.create_cars()

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT

    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False
