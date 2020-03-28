# -*- coding :  utf-8 -*-
# @Time      :  2020/3/18  22:20
# @author    :  沙漏在下雨
# @Software  :  PyCharm
import turtle as t

string = '这将绘制一个流彩扇'
print(string)


def draw():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    amy = t.Turtle()
    amy_w = t.Screen()
    amy_w.screensize(bg='snow')  # 背景  加速
    amy.getscreen().tracer(5)
    amy.speed(0)
    amy.hideturtle()
    for i in range(360):
        amy.color(colors[i % 6])
        amy.forward(i * 2)
        amy.right(181)
    amy_w.exitonclick()  # 点击关闭画布


if __name__ == '__main__':
    draw()
