import turtle


def main():
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.speed(10)
    t.color('red', 'yellow')
    make_art(t, 350)
    my_window.exitonclick()


def make_art(t, steps):
    if steps < 20:
        return
    t.begin_fill()
    while True:
        t.forward(steps)
        t.left(95)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    make_art(t, steps / 3)


if __name__ == "__main__":
    main()
