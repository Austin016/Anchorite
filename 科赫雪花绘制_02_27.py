# @Time : 2022/2/27 10:45 
# @Author : 818号
# -*- coding:utf-8 -*-
# @File : 科赫雪花绘制_02_27.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 4 # 定义阶数
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()
main()

