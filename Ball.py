from turtle import Turtle


DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.move_x = DISTANCE
        self.move_y = DISTANCE

    def change_direction_x(self):
        self.move_x *= -1

    def change_direction_y(self):
        self.move_y *= -1

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def reset_pos(self):
        self.goto(0, 0)
