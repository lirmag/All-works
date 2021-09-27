import turtle
import random

ran_color = []
print("Введите радиус окружности:")
r = int(input())
print("Введите список цветов:")

while True:
    elements = input()
    if elements:
        break
    else:
        ran_color.append(elements)

a = 1
t = turtle.Turtle()


def draw_circle(r):
    t.circle(r)
    while True:
        t.color(ran_color[random.randint(0, len(ran_color) - 1)])
        t.circle(r + 5)
        r = r + 5


draw_circle(r)
t.exitonclick()
