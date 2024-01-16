from turtle import Turtle


class Block(Turtle):
    def __init__(self, color_, x_pos, y_pos):
        super().__init__(shape="square", visible=False)
        self.penup()
        self.color(color_)
        self.goto(x_pos, y_pos)
        self.shapesize(stretch_len=4, stretch_wid=1, outline=1)
        self.showturtle()
