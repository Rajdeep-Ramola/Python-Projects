from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("green")
screen.title("Snake game")
screen.tracer(0) #turns automatic screen update on or off

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update() #to update the frame on screen which has been disabled by screen.tracer earlier
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15: #calculates distance of snake head from food
        food.refresh() #to shift food to new location
        snake.extend() #to increase the length of the snake
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:

      scoreboard.reset()
      snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]: #slicing to access specific section of a list or tuple
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10: #if distamce of head is less than 10 from other segments
            scoreboard.reset()


screen.exitonclick()



