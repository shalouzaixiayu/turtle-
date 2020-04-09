# 科赫雪花
import turtle as a


def koch(length, n):  # 长度 和 阶数
    if n == 0:
        t.fd(length)
    else:
        for i in [0, 60, -120, 60]:
            t.left(i)
            koch(length / 3, n - 1)


if __name__ == '__main__':
    t = a.Turtle()
    w = a.Screen()
    w.screensize(bg='wheat')
    t.speed(0)
    t.getscreen().tracer(10, 0)
    t.hideturtle()

    t.penup()
    t.pensize(2)
    t.goto(-200, 100)
    t.down()
    Leave = 8
    koch(400, Leave)
    t.right(120)
    koch(400, Leave)
    t.right(120)
    koch(400, Leave)
    t.right(120)
    w.exitonclick()
