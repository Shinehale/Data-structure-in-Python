import os
import sys
import math


class Fraction:
    def __init__(self, gnum, gden):
        common=math.gcd(gnum,gden)
        self.num = gnum//common
        self.den = gden//common

    def __gt__(self, other):
        return self.den * other.num < self.num * other.den

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __lt__(self, other):
        return self.num*other.den < self.den*other.num

    def __le__(self, other):
        return self.num*other.den <= self.den*other.num

    def __ne__(self, other):
        return self.num*other.den != self.den*other.num
