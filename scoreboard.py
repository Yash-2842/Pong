from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-40, 200)
        self.clear()
        self.write(self.l_score, False, "center", ("courier", 50, "bold"))
        self.goto(40, 200)
        self.write(self.r_score, False, "center", ("courier", 50, "bold"))

    def lscore(self):
        self.l_score += 1
        self.update()

    def rscore(self):
        self.r_score += 1
        self.update()
