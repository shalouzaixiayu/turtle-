#   正方形彩色螺旋线
import turtle as a

a.setup(600, 600)  # 画布尺寸   DIY
a.color("black")  # 画布颜色 DIY
a.begin_fill()
a.penup()
a.goto(-300, 300)  # 坐标 全部参照 你改画布尺寸计算
a.pendown()
a.goto(300, 300)
a.goto(300, -300)
a.goto(-300, -300)
a.goto(-300, 300)
a.end_fill()
a.penup()
a.goto(0, 0)
a.pendown()
a.pensize(1)
a.speed(98)
colors = ["purple", "red", "green", "blue"]  # 四元素 DIY
for i in range(450):
    a.pencolor(colors[i % 4])
    a.fd(2 * i)
    a.left(91)
a.hideturtle()
a.done()
