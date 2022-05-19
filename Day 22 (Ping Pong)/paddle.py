from turtle import Turtle
PADDLE_SIZE = 5


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_SIZE, stretch_len=0.5)
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)


class IA(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_SIZE, stretch_len=0.5)
        self.penup()
        self.goto(position)

    def move(self, ball_y):
        if ball_y > self.ycor() + 40:
            self.goto(self.xcor(), self.ycor() + 10)
        if ball_y < self.ycor() - 40:
            self.goto(self.xcor(), self.ycor() - 10)
