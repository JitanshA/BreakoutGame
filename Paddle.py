from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape="square", visible=False)
        self.penup()
        self.move_distance = 10
        self.color("cyan")
        self.goto(0, -280)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.showturtle()

    def move_left(self):
        if -285 < self.xcor():
            self.backward(self.move_distance)

    def move_right(self):
        if self.xcor() < 285:
            self.forward(self.move_distance)

    def shrink(self):
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
        self.move_distance *= 2

    def reset_pos(self):
        self.goto(0, -280)
