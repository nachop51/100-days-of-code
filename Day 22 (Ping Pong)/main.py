import time
from turtle import Screen
from paddle import Paddle, IA
from ball import Ball
from scoreboard import Scoreboard
WIDTH = 800
HEIGHT = 600
POSITION = [(20 - 800 / 2, 0), (800 / 2 - 20, 0)]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Ping pong")
screen.tracer(0)

l_paddle = Paddle(POSITION[0])
r_paddle = IA(POSITION[1])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, key="Up")
screen.onkeypress(l_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    # Bounce
    if ball.ycor() > HEIGHT / 2 - 20 or ball.ycor() < -HEIGHT / 2 - 20:
        ball.bounce_y()
    if ball.xcor() < -WIDTH / 2 + 40 and ball.distance(l_paddle) < 50 or ball.xcor() > WIDTH / 2 - 40 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    # Players score
    if ball.xcor() > WIDTH / 2 - 10:
        scoreboard.increase_l_score()
        ball.reset_position()
        if scoreboard.l_score >= 3:
            game_is_on = False
    if ball.xcor() < -WIDTH / 2 - 10:
        scoreboard.increase_r_score()
        ball.reset_position()
        if scoreboard.r_score >= 3:
            game_is_on = False
    r_paddle.move(ball.ycor())
    ball.move()
    time.sleep(ball.move_speed)

screen.exitonclick()
