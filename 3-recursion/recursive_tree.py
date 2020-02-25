import turtle
import random


def tree(branch_len, pen_width, t):
    if branch_len > 5:
        rand_branch_len1 = random.randrange(5, 20)
        rand_branch_len2 = random.randrange(5, 20)
        right_angle = random.randrange(15, 46)
        left_angle = right_angle * 2

        t.color("green") if branch_len < 20 else t.color("brown")
        t.pensize(width=pen_width)
        t.forward(branch_len)
        t.right(right_angle)
        tree(branch_len - rand_branch_len1, max(1, pen_width - 2), t)
        t.left(left_angle)
        tree(branch_len - rand_branch_len2, max(1, pen_width - 2), t)
        t.right(right_angle)
        t.pensize(width=pen_width)
        t.color("green") if branch_len < 30 else t.color("brown")
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, 10, t)
    my_window.exitonclick()


main()
