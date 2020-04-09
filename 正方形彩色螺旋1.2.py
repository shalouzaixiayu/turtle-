import turtle as a

colors = ["red", "blue", "green"]
a.pensize(1)
a.speed(0)
for i in range(800):
    a.fd(i * 2)
    a.pencolor(colors[i % 3])
    a.right(121)
a.hideturtle()
a.done()
