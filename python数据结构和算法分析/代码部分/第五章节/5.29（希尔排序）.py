import random
import timeit


def shellSort(Lis,delta):
    sublistcount = len(Lis) // delta
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(Lis, startposition, sublistcount)
        sublistcount //= delta


def gapInsertionSort(Lis, start, gap):
    for i in range(start + gap, len(Lis), gap):
        currentValue = Lis[i]
        position = i
        while position >= gap and \
                Lis[position - gap] > currentValue:
            Lis[position] = Lis[position - gap]
            position = position - gap
        Lis[position] = currentValue


def generate(List):
    for i in range(100000):
        newValue = random.randint(1, 5000)
        List.append(newValue)


alist = []
generate(alist)
Lis1,Lis2=alist,alist
t1=timeit.Timer("shellSort(Lis1,13)","from __main__ import Lis1,shellSort")
t2=timeit.Timer("shellSort(Lis2,167)","from __main__ import Lis2,shellSort")
fir_time=t1.timeit(number=1)
sec_time=t2.timeit(number=1)
print(fir_time,sec_time)
# >> 1.6542141000027186 0.05701979999867035
"""
数集越大
运行速度越快并且完成度越高
"""