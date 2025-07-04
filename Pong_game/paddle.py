from turtle import Turtle


class Paddle(Turtle): #paddle class inherits from turtle
    def __init__(self,position ):  #arguement for position of paddle
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


# function to move the paddle up and down
    def go_up(self):
     new_y =self.ycor() + 20
     self.goto(self.xcor(), new_y)



    def go_down(self):
     new_y = self.ycor() - 20
     self.goto(self.xcor(), new_y)
