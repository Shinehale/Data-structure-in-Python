"""
更改之后的冒泡排序
奇数次获得未确定序列中未排完的最大值的位置
但是偶数次获得未确定序列中未拍完的最小值的位置
适用于渴望单次获得最大值最小值的情况
"""

import random


def bubbleSort(List):
    L, R = 0, len(List) - 1
    for passnum in range(len(List) - 1, 0, -1):
        if (passnum - len(List) + 1) % 2:
            for i in range(R - 1, L - 1, -1):
                if List[i + 1] < List[i]:
                    List[i], List[i + 1] = List[i + 1], List[i]
            L = L + 1
        else:
            for i in range(L, R, 1):
                if List[i] > List[i + 1]:
                    List[i], List[i + 1] = List[i + 1], List[i]
            R = R - 1
        print(List)


def generate(alist):
    for i in range(30):
        newValue = random.randint(1, 5000)
        alist.append(newValue)


alist = []
generate(alist)
print("排序前的数组：\n", alist)
bubbleSort(alist)
print("排序后的数组：\n", alist)
