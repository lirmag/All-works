import turtle
import random

a = 1
t = turtle.Turtle()
ran_color = ["red", "brown", "pink", "blue", "magenta", "black", "yellow"]


def draw_circle(r):
    t.circle(r)
    while True:
        t.color(ran_color[random.randint(0, len(ran_color) - 1)])
        t.circle(r + 5)
        r = r + 5


draw_circle(40)
t.exitonclick()
