import os
import sys
import math


class Fraction:
    def __init__(self, gnum, gden):
        common=math.gcd(gnum,gden)
        self.num = gnum//common
        self.den = gden//common

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum == secondNum

    def __add__(self, other):# 重载了加的操作
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other): #重载了减的操作
        common=self.den*other.den
        newNum=self.num*other.den-other.num*self.den
        return Fraction(newNum,common)

    def __mul__(self, other): #重载了*的操作
        newNum=self.num*other.num
        newDen=self.den*other.den
        return Fraction(newNum,newDen)

    def __truediv__(self, other): #重载了/的操作
        newNum = self.num * other.den
        newDen = self.den * other.num
        return Fraction(newNum, newDen)

    def show(self):
        print(str(self.num)+"/"+str(self.den))

m,n=map(int,input().split())
frac=Fraction(m,n)
fr=Fraction(n,m)
(frac*fr).show()
(frac-fr).show()
(frac/fr).show()
