import turtle
import random

t = turtle.Turtle()
ran_color = ["red", "brown", "pink", "blue", "magenta", "black", "yellow"]


def snowball_1(r):
    t.color(random.choice(ran_color))
    t.circle(- r)
    t.color(random.choice(ran_color))
    t.circle(0.8 * r)
    t.up()
    t.goto(0, 1.6 * r)
    t.down()
    t.color(random.choice(ran_color))
    t.circle(0.7 * r)


def eyes_1(y):
    t.color("black")
    t.up()
    t.goto(40, 240)
    t.down()
    t.circle(7)
    t.up()
    t.goto(-40, 240)
    t.down()
    t.circle(7)


def nose_1(forward):
    t.color("orange")
    t.up()
    t.goto(-10, 215)
    t.down()
    t.left(90)
    t.forward(20)
    t.right(100)
    t.forward(forward)
    t.right(155)
    t.forward(forward)
    t.up()
    t.right(115)
    turtle.up()


def centre_1(y):
    turtle.goto(0, y)
    turtle.down()
    turtle.circle(10)
    for circle in range(2):
        y += 20
        turtle.up()
        turtle.goto(0, y)
        turtle.down()
        turtle.circle(10)


snowball_1(100)
eyes_1(50)
nose_1(50)
centre_1(50)
turtle.exitonclick()
