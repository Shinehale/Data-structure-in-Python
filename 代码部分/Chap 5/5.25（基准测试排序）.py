import timeit
import random


def selectionSort(List):
    for fillSlot in range(len(List) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillSlot + 1):
            if List[location] > List[positionOfMax]:
                positionOfMax = location
        List[fillSlot], List[positionOfMax] = List[positionOfMax], List[fillSlot]


def generate(List):
    for i in range(10000):
        newValue = random.randint(1, 5000)
        List.append(newValue)


alist = []
generate(alist)
t1 = timeit.Timer("sortList=sorted(alist)", "from __main__ import alist")
t2 = timeit.Timer("selectionSort(alist)", "from __main__ import alist,selectionSort")
sortList = sorted(alist)
fir_time = t1.timeit(number=1)
sec_time = t2.timeit(number=1)
print("排序后的数组：\n", sortList)
print(fir_time,sec_time)
# >> 0.00013519999993150122 6.066131600000517
# >> 处理N=100000 时 0.03211390000069514
"""
从结果中不难看出
O(n log n )算法的sort速度明显是手写的算法的无数倍
"""