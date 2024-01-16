from turtle import Turtle


FONT_TUPLE = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(200, 280)
        self.pencolor("white")
        self.score = 0
        self.lives = 3
        self.write_score()

    def write_score(self):
        self.write(f"SCORE: {self.score} LIVES: {self.lives}", move=False, align="center", font=FONT_TUPLE)

    def update_score(self, points):
        self.score += points
        self.clear()
        self.write_score()

    def decrement_lives(self):
        self.lives -= 1
        self.clear()
        self.write_score()

    def game_over(self):
        if self.lives == 0:
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER\nSCORE: {self.score}\nBetter Luck Next Time!", move=False, font=FONT_TUPLE, align="center")
        else:
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER\nSCORE: {self.score}\nWell Done!", move=False, font=FONT_TUPLE, align="center")
