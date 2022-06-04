from turtle import *
import random

def tree(branchLen, t):
    if branchLen > 15:
        t.color("brown")
        t.pensize(branchLen//10)
        t.forward(branchLen)
        ranRange1=random.randint(15,25)
        t.right(ranRange1)
        newValue=random.randint(11,15)
        tree(branchLen - newValue, t)
        ranRange2=random.randint(35,45)
        t.left(ranRange2)
        newValue=random.randint(8,10)
        tree(branchLen - newValue, t)
        t.right(ranRange2-ranRange1)
        t.backward(branchLen)
    else:
        t.color("green")
        t.pensize(branchLen//10+2)

tracer(False)
t = Turtle()
myWin = t.getscreen()
t.speed(10)
t.left(90)
t.up()
t.backward(300)
t.down()
t.color("brown")
tree(110, t)
myWin.exitonclick()
