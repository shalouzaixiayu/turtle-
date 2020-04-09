# 爱心
import turtle as a

a.setup(800, 500, 100, 100)
a.pensize(6)
a.speed(89)
a.color("red", "pink")
a.begin_fill()
a.left(135)
a.fd(140)
for i in range(200):
    a.right(1)
    a.fd(1)
a.left(135)
for i in range(200):
    a.right(1)
    a.fd(1)
a.fd(140)
a.end_fill()
a.hideturtle()
a.done()
