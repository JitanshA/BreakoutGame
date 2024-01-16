from turtle import Screen
from Paddle import Paddle
from ScoreBoard import ScoreBoard
from Ball import Ball
from Block import Block
import time


COLORS = ['yellow', 'green', 'orange', 'red']
blocks = []
block_coords_list = []

sleep_speed = 0.08
speed_count = 0
points = 1


def generate_wall():
    x_pos = -300
    y_pos = 180
    for i in range(4):
        for j in range(8):
            blocks.append(Block(color_=COLORS[i], x_pos=x_pos, y_pos=y_pos))
            block_coords_list.append((x_pos, y_pos))
            x_pos += 90
        y_pos += 30
        x_pos = -300


def check_for_blocks():
    for i in range(len(block_coords_list)):
        if my_ball.xcor() - 40 <= block_coords_list[i][0] <= my_ball.xcor() + 40 and my_ball.ycor() - 15 <= block_coords_list[i][1] <= my_ball.ycor() + 15:
            blocks[i].hideturtle()
            block_color = blocks[i].color()[1]
            global points
            if block_color == "yellow":
                points = 1
            elif block_color == "green":
                points = 3
            elif block_color == "orange":
                points = 5
            elif block_color == "red":
                points = 7
            blocks[i].goto(1000, 1000)
            blocks.remove(blocks[i])
            block_coords_list.remove(block_coords_list[i])
            return True

    return False


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.screensize(canvwidth=600, canvheight=600)

my_screen.tracer(0, 0)

my_paddle = Paddle()
my_score_board = ScoreBoard()
my_ball = Ball()

generate_wall()

my_screen.update()

game_is_on = True

while game_is_on:
    time.sleep(sleep_speed)
    my_ball.move()

    if my_ball.ycor() > 170:
        collision = check_for_blocks()
        if collision:
            my_ball.change_direction_y()
            my_score_board.update_score(points)
            if my_score_board.score >= 72 and speed_count != 1:
                sleep_speed -= 0.05
                speed_count = 1
                my_paddle.shrink()

    if my_ball.xcor() >= 330 or my_ball.xcor() <= -330:
        my_ball.change_direction_x()

    if -280 < my_ball.ycor() < -260 and my_ball.distance(my_paddle) <= 50:
        my_ball.change_direction_y()

    if my_ball.ycor() >= 280:
        my_ball.change_direction_y()

    if my_ball.ycor() <= -300:
        my_ball.reset_pos()
        my_score_board.decrement_lives()
        my_paddle.reset_pos()

    if my_score_board.score == 128 or my_score_board.lives == 0:
        game_is_on = False
        my_score_board.game_over()
        my_ball.hideturtle()

    my_screen.onkeypress(my_paddle.move_left, "Left")
    my_screen.onkeypress(my_paddle.move_right, "Right")
    my_screen.listen()
    my_screen.update()

my_screen.exitonclick()
my_screen.mainloop()
