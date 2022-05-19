from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-290, 260)
        self.level = 1
        self.print_score()

    def increment_level(self):
        self.level += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-60, -10)
        self.write("GAME OVER!", font=FONT)
