import turtle as t
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.pendown()
for i in range(3, 11):
    t.color(choice(colours))
    for x in range(i):
        angle = 360 / i
        t.forward(100)
        t.right(angle)

t.done()
t.bye()
