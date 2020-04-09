# -*- coding :  utf-8 -*-
# @Time      :  2020/3/5  23:23
# @author    :  沙漏在下雨
# @Software  :  PyCharm
import turtle as T
import random

size_n = 10


def draw_tree(brance):  # 画树枝部分
    if brance > 4:
        if 8 <= brance <= 16:
            if random.randint(0, 2) == 0:
                t.pencolor("snow")
            else:
                t.pencolor("lightcoral")  # 珊瑚色
            t.pensize(brance / 4)
        elif brance < 8:
            if random.randint(0, 1) == 0:
                t.pencolor("snow")
            else:
                t.pencolor("lightcoral")  # 珊瑚色
            t.pensize(brance / 2)
        else:
            t.pencolor("Tan")  # 褐色
            t.pensize(brance / 10)  # 缩小支柱
        t.fd(brance)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        draw_tree(brance - 10 * b)  # 往右画，直到画不动为止，然后左转随机度数
        t.left(40 * a)  # 左转
        draw_tree(brance - 10 * b)  # 往左画，直到画不动为止，然后右转随机度数
        t.right(20 * a)
        t.penup()
        t.backward(brance)
        t.pendown()


def draw_tree1(brance):  # 画树枝部分
    if brance > size_n:  # 画右边
        t.fd(brance)
        t.right(30)
        draw_tree1(brance / 1.5)  # 继续画右边的 走不动了往左边转40
        # 画左边
        t.left(60)
        draw_tree1(brance / 1.5)  # 继续画左边的，走不动了右转20回到原树枝
        # 回到之前的树枝
        t.right(30)
        # 给最后二个树枝画叶子
        if brance / 1.5 <= size_n:
            t.pencolor("snow")
        else:
            t.pencolor("Tan")
        t.backward(brance)


def petel(m):  # m为循环次数   绘制树叶
    t.pensize(2)
    for i in range(m):
        a = 250 - 500 * random.random()  # 树叶长度，有正有负，可以确定海龟走二个方向
        b = 10 - 20 * random.random()  # 树叶宽度
        t.penup()
        t.fd(b)
        t.left(90)
        t.fd(a)
        t.pendown()
        t.pencolor("lightcoral")  # 珊瑚色
        t.circle(1)
        t.penup()
        t.backward(a)
        t.right(90)
        t.backward(b)


t = T.Turtle()
w = T.Screen()
w.screensize(bg='wheat')  # 画布颜色小麦色
# t.speed(0)  # 速度最快
t.getscreen().tracer(5, 0)  # 返回正在绘制的对象 并且加速5
t.pensize(5)
t.left(90)
t.penup()
t.backward(250)
t.pendown()
t.color("Tan")  # 褐色
draw_tree(70)  # 第一颗桃花，支柱设置80
petel(250)  # 花瓣250
w.exitonclick()  # 点击关闭画布
