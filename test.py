import turtle
y = 20
for circle in range(3):
    turtle.circle(10)
    turtle.up()
    turtle.goto(0, y)
    turtle.down()
    y += 20
turtle.exitonclick()