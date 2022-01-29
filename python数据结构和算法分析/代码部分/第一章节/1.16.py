import os
import sys
import math


class Fraction:
    def __init__(self, gnum, gden):
        common=math.gcd(gnum,gden)
        self.num = gnum//common
        self.den = gden//common

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum == secondNum

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

m,n=map(int,input().split())
frac=Fraction(m,n)
print(frac.getNum())
print(frac.getDen())
