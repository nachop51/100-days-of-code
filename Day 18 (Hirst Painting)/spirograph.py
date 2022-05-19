import turtle as t
from random import choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


t.colormode(255)
tim = t.Turtle()
tim.speed(200)
for i in range(0, 361, 3):
    tim.seth(i)
    tim.circle(100)
    tim.color(random_color())

t.done()