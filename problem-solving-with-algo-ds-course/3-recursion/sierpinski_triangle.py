import turtle


def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sier(points, degree, t):
    color_map = ['blue', 'red', 'white', 'yellow', 'orange', 'purple']
    draw_triangle(points, color_map[degree], t)
    if degree > 0:
        sier([points[0], get_mid(points[0], points[1]),
              get_mid(points[0], points[2])], degree - 1, t)
        sier([points[1], get_mid(points[0], points[1]),
              get_mid(points[1], points[2])], degree - 1, t)
        sier([points[2], get_mid(points[2], points[1]),
              get_mid(points[0], points[2])], degree - 1, t)


def main():
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.speed(1)
    points = [[-150, -100], [0, 150], [150, -100]]
    sier(points, 5, t)
    my_window.exitonclick()


main()
