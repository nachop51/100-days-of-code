from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.print_score()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.print_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)

