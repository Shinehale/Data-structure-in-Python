"""
分区限制
当当前的列表长度小于10时
自动进行插入排序
而别的情况下直接进行快速排序
"""
import random


def quickSort(Lis):
    quickSortHelper(Lis, 0, len(Lis) - 1)


def insertionSort(L,R,Lis):
    for i in range(1,(R-L+1)):
        currentValue=Lis[L+i]
        position=L+i
        while position>L and Lis[position-1]> currentValue:
            Lis[position]=Lis[position-1]
            position=position-1
        Lis[position]=currentValue


def quickSortHelper(Lis, first, last):
    if last-first>10:
        splitpoint = partition(Lis, first, last)
        quickSortHelper(Lis, first, splitpoint - 1)
        quickSortHelper(Lis, splitpoint + 1, last)
    else:
        insertionSort(first,last,Lis)


def partition(Lis, first, last):
    pivotvalue = Lis[first]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and \
                Lis[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while Lis[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            Lis[leftmark], Lis[rightmark] = Lis[rightmark], Lis[leftmark]

    Lis[first], Lis[rightmark] = Lis[rightmark], Lis[first]

    return rightmark


def generate(List):
    for i in range(2000):
        newValue = random.randint(1, 5000)
        List.append(newValue)


alist = []
generate(alist)
quickSort(alist)
print(alist)
