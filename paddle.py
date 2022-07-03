from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.penup()
        self.color("white")
        self.setpos(pos, 0)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)
