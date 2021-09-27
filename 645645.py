import turtle

t = turtle.Turtle()


def draw_snowball(r, color, steps):
    t.color(color)
    t.circle(r)
    t.up()
    t.goto(0, 2 * steps)
    t.down()


draw_snowball(50, "red" , 50)
draw_snowball(40, "purple" , 90)
draw_snowball(30, "pink" , 0)
t.up()
t.goto(0,-60)
t.down
t.circle(20)

turtle.exitonclick()
