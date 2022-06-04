import random


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def generate(alist):
    for i in range(500):
        newValue = random.randint(1, 5000)
        alist.append(newValue)


alist = []
generate(alist)
print("排序前的数组：\n", alist)
bubbleSort(alist)
print("排序后的数组：\n", alist)
