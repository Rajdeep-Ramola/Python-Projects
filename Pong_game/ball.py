from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    #move the ball in the screen
    def move(self):
      new_x=self.xcor()+self.x_move
      new_y=self.ycor()+self.y_move
      self.goto(new_x,new_y)
    #to bounce the ball on the upper and lower wall
    def bouncey(self):
        self.y_move *= -1

    #to bounce the ball with paddle
    def bouncex(self):
        self.x_move *= -1
        self.move_speed *=0.9

    #to reset the position of ball if ball is out of the screen
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bouncex()