import turtle as t
from random import choice, randint
# import colorgram
# # This works to extract colors from an image
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(211, 159, 85), (188, 176, 33), (172, 50, 71), (233, 71, 36),
              (153, 30, 44), (229, 208, 110), (66, 34, 55), (193, 71, 38),
              (126, 164, 193), (212, 131, 162), (212, 66, 111), (55, 50, 108),
              (58, 85, 151), (41, 38, 69), (49, 135, 95), (111, 182, 157),
              (144, 32, 27), (56, 165, 186), (45, 159, 105), (83, 52, 34),
              (150, 203, 220), (86, 99, 178), (228, 166, 182), (234, 172, 163),
              (170, 206, 184), (182, 185, 213)]
t.colormode(255)
tim = t.Turtle()
tim.speed(200)
tim.penup()
tim.hideturtle()
for i in range(0, 500, 50):
    tim.goto(-225, i - 225)
    for j in range(0, 500, 50):
        tim.dot(20, choice(color_list))
        tim.forward(50)
t.done()
