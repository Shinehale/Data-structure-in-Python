from turtle import *


def hilbert(n, m):
    if n == 1:
        tur.forward(x)
        tur.right(180 * m + 90)
        tur.forward(x)
        tur.right(180 * m + 90)
        tur.forward(x)
    else:
        tur.right(180 * m + 90)
        hilbert(n - 1, 1 - m)
        tur.right(180 * m + 90)
        tur.forward(x)
        hilbert(n - 1, m)
        tur.right(180 * (1 - m) + 90)
        tur.forward(x)
        tur.right(180 * (1 - m) + 90)
        hilbert(n - 1, m)
        tur.forward(x)
        tur.right(180 * m + 90)
        hilbert(n - 1, 1 - m)
        tur.right(180 * m + 90)


tur = Turtle()
tur.speed(200)
myWin = tur.getscreen()
N = int(input("请输入你想要实现的希尔伯特曲线阶数:\n"))
Step = 200
x = Step / (2 * N + 1)
tur.left(90)
tur.up()
tur.goto(-200, -200)
tur.down()
hilbert(N, 0)
myWin.exitonclick()
