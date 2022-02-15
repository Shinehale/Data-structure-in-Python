from turtle import *


def koch(step, size):
    if size == 0:
        tur.forward(step)
    else:
        for angle in [0, 60, -120, 60]:
            tur.left(angle)
            koch(step / 3, size - 1)


N = int(input("请输入你要获得雪花的阶数:\n"))
tur = Turtle()
tracer(False)
myWin = tur.getscreen()
length = 400
tur.up()
tur.speed(1000)
tur.goto(-200, 100)
tur.down()
tur.pensize(3)
koch(length, N)
tur.right(120)
koch(length, N)
tur.right(120)
koch(length, N)
myWin.exitonclick()
