import os
import sys
import math


class Fraction:
    def __init__(self, gnum, gden):
        self.num = gnum
        self.den = gden

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
        return firstNum == secondNum

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = math.gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

n,m=map(int,input().split())
frac=Fraction(n,m)
print(frac.getDen())
print(frac.getNum())
