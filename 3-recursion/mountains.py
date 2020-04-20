import turtle
import random


def draw_mountains(height, t):
    draw_triangle(height, t)
    if height > 100:
        draw_mountains(height / 1.5, t)
        draw_mountains(height / 2, t)
        draw_mountains(height / 5, t)


def draw_triangle(height, t):
    t.down()
    colors = ['#cccccc', '#808080', '#4d4d4d', '#f2f2f2', '#737373', '#000000']
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for _ in range(3):
        t.forward(height)
        t.left(120)
    t.end_fill()
    t.setheading(0)
    t.up()
    t.goto(random.randint(-600, 500), -200)


def main():
    height = 600
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.speed(10)
    t.up()
    t.goto(-300, -200)
    t.setheading(0)
    draw_mountains(height, t)
    my_window.exitonclick()


main()
