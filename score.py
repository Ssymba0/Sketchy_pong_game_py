from turtle import Turtle
alignment = 'center'
font = ('Calibri', 40, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.up()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(self.left_score, align=alignment, font=font)
        self.goto(100, 240)
        self.write(self.right_score, align=alignment, font=font)

    def left_increment(self):
        self.clear()
        self.left_score += 1
        self.update_score()

    def right_increment(self):
        self.clear()
        self.right_score += 1
        self.update_score()
