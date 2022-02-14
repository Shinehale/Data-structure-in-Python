"""
抱歉，网上没有找到相关的资料
一些文件也确实没有详细说明分形山最终是怎么形成的
就此搁笔，等有能力看到更好的实现方法再来补充
"""

from turtle import *
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def calc(self, p2):
        ans = Point()
        ans.x = (self.x + p2.getX()) / 2
        ans.y = (self.y + p2.getY()) / 2
        return ans


def mountain(size, p1, p2, p3):
    if size == 0:
        return
    mid1 = p1.calc(p2)
    mid2 = p2.calc(p3)
    mid3 = p3.calc(p1)
    mountain(size - 1, p1, mid1, mid3)
    mountain(size - 1, mid1, p2, mid2)
    mountain(size - 1, mid3, mid2, p3)
    mountain(size-1,mid2, mid1, mid3)
    t.up()
    t.goto(p1.getX(),p1.getY())
    newValue=random.randint(1,6)


t = Turtle()
myWin = t.getscreen()
P1 = Point(0, 200)
P2 = Point(-173, -100)
P3 = Point(173, -100)
mountain(100, P1, P2, P3)
myWin.exitonclick()
