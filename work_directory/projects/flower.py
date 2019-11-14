# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2019/11/13 17:11
# # @Author  : Xiang Yu
# # @File    : flower.py
# # @Software: PyCharm
# # @Company : BEIJING INTENGINE


import math
import random
import turtle as t


list1 = []
for i in range(5):
    list1.append(int(random.uniform(-500, 500)))
list2 = []
for i in range(5):
    list2.append(int(random.uniform(-200, -50)))
list3 = []
for i in range(8):
    list3.append(int(random.uniform(-400, 400)))
list4 = []
for i in range(8):
    list4.append(int(random.uniform(-150, -50)))
list5 = []
for i in range(7):
    list5.append(int(random.uniform(-300, 300)))
list6 = []
for i in range(7):
    list6.append(int(random.uniform(-200, -100)))
list7 = []
for i in range(18):
    list7.append(int(random.uniform(-500, 500)))
list8 = []
for i in range(18):
    list8.append(int(random.uniform(-100, 100)))
# 绘制人名
t.speed(0)
t.penup()
t.goto(-290, 200)
t.pendown()
t.color("black")
t.forward(30)
t.backward(15)
t.right(90)
t.forward(45)
t.penup()
t.goto(-250, 170)
t.pendown()
t.circle(15, 180)
t.forward(15)
t.circle(15, 180)
t.forward(15)
t.penup()
t.goto(-200, 190)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.pencolor("black")
t.circle(3, 360)
t.penup()
t.goto(-200, 170)
t.pendown()
t.circle(3, 360)
t.end_fill()
t.penup()
t.goto(-190, 200)
t.pendown()
t.left(45)
t.forward(25)
t.penup()
t.goto(-155, 200)
t.pendown()
t.right(90)
t.forward(25)
t.left(45)
t.forward(30)
t.penup()
t.goto(-150, 170)
t.pendown()
t.circle(15, 180)
t.forward(15)
t.circle(15, 180)
t.forward(15)
t.penup()
t.goto(-135, 170)
t.pendown()
t.left(55)
t.forward(25)
t.penup()
t.goto(0, 0)
t.left(35)  # 将画笔设置到初始化位置

# 画大号爱心（位置随机）
for x, y in list(zip(list1, list2)):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#FF6A6A")
    t.begin_fill()
    t.pencolor("#FF6A6A")
    t.forward(40)
    t.circle(20, 180)
    t.right(90)
    t.circle(20, 180)
    t.forward(40)
    t.end_fill()
    t.penup()
    t.goto(x, y)
# 画中号爱心（位置随机）
for x, y in list(zip(list5, list6)):
    t.pendown()
    t.fillcolor("#FFA07A")
    t.begin_fill()
    t.pencolor("#FFA07A")
    t.forward(30)
    t.circle(15, 180)
    t.right(90)
    t.circle(15, 180)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.goto(x, y)
# 画小号爱心（位置随机）
for x, y in list(zip(list3, list4)):
    t.pendown()
    t.fillcolor("#FFD39B")
    t.begin_fill()
    t.pencolor("#FFD39B")
    t.forward(20)
    t.circle(10, 180)
    t.right(90)
    t.circle(10, 180)
    t.forward(20)
    t.end_fill()
    t.penup()
    t.goto(x, y)
# 画点点（位置随机）
for x, y in list(zip(list7, list8)):
    t.pendown()
    t.fillcolor("#FF6A6A")
    t.begin_fill()
    t.pencolor("#FF6A6A")
    t.circle(3, 360)
    t.end_fill()
    t.penup()
    t.goto(x, y)


def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))


# 初始位置设定
s = 0.2
# t.setup(450*5*s, 750*5*s)
t.pencolor("black")
t.fillcolor("#FF4040")
t.speed(100)
t.penup()
t.goto(0, 900 * s)
t.pendown()
# 绘制花朵形状
t.begin_fill()
t.circle(200 * s, 30)
DegreeCurve(60, 50 * s)
t.circle(200 * s, 30)
DegreeCurve(4, 100 * s)
t.circle(200 * s, 50)
DegreeCurve(50, 50 * s)
t.circle(350 * s, 65)
DegreeCurve(40, 70 * s)
t.circle(150 * s, 50)
DegreeCurve(20, 50 * s, -1)
t.circle(400 * s, 60)
DegreeCurve(18, 50 * s)
t.fd(250 * s)
t.right(150)
t.circle(-500 * s, 12)
t.left(140)
t.circle(550 * s, 110)
t.left(27)
t.circle(650 * s, 100)
t.left(130)
t.circle(-300 * s, 20)
t.right(123)
t.circle(220 * s, 57)
t.end_fill()
# 绘制花枝形状
t.left(120)
t.fd(280 * s)
t.left(115)
t.circle(300 * s, 33)
t.left(180)
t.circle(-300 * s, 33)
DegreeCurve(70, 225 * s, -1)
t.circle(350 * s, 104)
t.left(90)
t.circle(200 * s, 105)
t.circle(-500 * s, 63)
t.penup()
t.goto(170 * s, -30 * s)
t.pendown()
t.left(160)
DegreeCurve(20, 2500 * s)
DegreeCurve(220, 250 * s, -1)
# 绘制一个绿色叶子
t.fillcolor('#00CD00')
t.penup()
t.goto(670 * s, -180 * s)
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300 * s, 120)
t.left(60)
t.circle(300 * s, 120)
t.end_fill()
t.penup()
t.goto(180 * s, -550 * s)
t.pendown()
t.right(85)
t.circle(600 * s, 40)
# 绘制另一个绿色叶子
t.penup()
t.goto(-150 * s, -1000 * s)
t.pendown()
t.begin_fill()
t.rt(120)
t.circle(300 * s, 115)
t.left(75)
t.circle(300 * s, 100)
t.end_fill()
t.penup()
t.goto(430 * s, -1070 * s)
t.pendown()
t.right(30)
t.circle(-600 * s, 35)

t.done()


# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator
#
# from matplotlib.font_manager import FontProperties
# # 用于解决 Windows 系统，显示中文字体的问题
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=45)
#
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# [x, t] = np.meshgrid(np.array(range(25))/24.0, np.arange(0, 575.5, 0.5)/575*17*np.pi - 2*np.pi)
# p = np.pi/2 * np.exp(-t/(8*np.pi))
# u = 1 - (1 - np.mod(3.6*t, 2 * np.pi)/np.pi) ** 4/2
# y = 2 * (x ** 2-x)**2*np.sin(p)
# r = u * (x*np.sin(p) + y * np.cos(p))
#
# surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), u * (x*np.cos(p)-y*np.sin(p)),
#                         rstride=10, cstride=10 ** 10, cmap=cm.gist_heat, linewidth=7,
#                        antialiased=True
#                        )
#
# plt.title(u'无聊的yipi！', fontproperties=font)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
# plt.show()
#
