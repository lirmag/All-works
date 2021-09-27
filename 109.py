import turtle
import  time
l = 200
for i in range(2):
    turtle.forward(l)
    turtle.left(90)
while l != 0:
    turtle.forward(l-10)
    turtle.left(90)
    l -= 10
time.sleep(1000)