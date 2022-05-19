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
tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
rotate = [0, 90, 180, 270]
tim.width(15)
tim.speed(200)
for i in range(300):
    tim.color(random_color())
    tim.seth(choice(rotate))
    tim.forward(30)

t.done()
