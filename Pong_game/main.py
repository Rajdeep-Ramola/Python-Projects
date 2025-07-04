from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time
#setting up screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800,600)
screen.tracer(0) #turn screen update or animation off
#creating a paddle
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()




#using keys to move the paddle
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
      ball.bouncey()

    #detecting collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bouncex()

    #detect r_paddle miss
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #detect l_paddle miss
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()

