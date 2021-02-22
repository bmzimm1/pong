from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Board
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("All-American Ping-Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_score = Board(alignment="right", y=260, x=340)
l_score = Board(alignment="left", y=260, x=-340)
ball = Ball()
cheats = screen.textinput("Cheats", "Enter any cheats now.")
if cheats == 'konami':
    screen.bgpic('fahrest.gif')
else:
    screen.bgcolor("black")

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, 'Down')

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        l_score.increase_score("left")
        ball.reset_position()

    elif ball.xcor() < -380:
        r_score.increase_score("right")
        ball.reset_position()

screen.exitonclick()
