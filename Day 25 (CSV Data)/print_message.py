from turtle import Turtle
import pandas


class PrintMessage(Turtle):
    def __init__(self):
        super(PrintMessage, self).__init__()
        self.hideturtle()
        self.penup()

    def print_this(self, states):
        state = states.to_dict()
        for i in range(51):
            try:
                name = state["state"][i]
            except Exception:
                continue
        cord_x = int(states["x"])
        cord_y = int(states["y"])
        self.goto(cord_x, cord_y)
        self.write(name)

