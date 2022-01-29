import os
import sys
import math


class Fraction:
    def __init__(self, gnum, gden):
        if not isinstance(gnum,int) or not isinstance(gden,int):
            print("error")
        else:
            common = math.gcd(gnum, gden)
            self.num = gnum // common
            self.den = gden // common

    def show(self):
        print(str(self.num)+"/"+str(self.den))

R=input().split()
n,m=eval(R[0]),eval(R[1])
fc=Fraction(n,m)