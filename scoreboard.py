from turtle import Turtle

FONT = ("courier", 24, "normal")


class Board(Turtle):
    def __init__(self, alignment, x, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.write(f"Score: {self.score}", align=alignment, font=FONT)

    def increase_score(self, alignment):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=alignment, font=FONT)
