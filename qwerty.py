import turtle

t = turtle.Turtle


def snowball(r, color):
    t.color(color)
    t.circle(r)


snowball(200, "red")
t.goto(0, 200)
snowball(150, "purple")

turtle.exitonclick()
