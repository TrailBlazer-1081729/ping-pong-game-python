from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")

screen.tracer(0)
paddle_r=Paddle(370,0)
paddle_l=Paddle(-370,0)
ball=Ball()
score=Score()

# screen.update()
check_game=True
def over():
    global check_game
    check_game=False


screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")
screen.onkey(over,"e")


while check_game:
    time.sleep(ball.move_s)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(paddle_r)<45 and ball.xcor()>350 or ball.distance(paddle_l)<45 and ball.xcor()<-350:
        ball.bounce_x()
    if ball.xcor()>390:
        ball.reset_r()
        score.l_point()
    if ball.xcor()<-390:
        ball.reset_r()
        score.r_point()













screen.exitonclick()
