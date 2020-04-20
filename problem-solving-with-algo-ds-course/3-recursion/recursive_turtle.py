import turtle

my_turtle = turtle.Turtle()
my_window = turtle.Screen()


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 2.5)


draw_spiral(my_turtle, 250)
my_window.exitonclick()
