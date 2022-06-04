"""
取三中值作为基准进行排序
防止算法复杂度退化到O(n^2)
"""
import random


def quickSort(Lis):
    quickSortHelper(Lis, 0, len(Lis) - 1)


def insertionSort(L, R, Lis):
    for i in range(1, (R - L + 1)):
        currentValue = Lis[L + i]
        position = L + i
        while position > L and Lis[position - 1] > currentValue:
            Lis[position] = Lis[position - 1]
            position = position - 1
        Lis[position] = currentValue


def quickSortHelper(Lis, first, last):
    if last - first > 0:
        splitpoint = partition(Lis, first, last)
        quickSortHelper(Lis, first, splitpoint - 1)
        quickSortHelper(Lis, splitpoint + 1, last)


def partition(Lis, first, last):
    pivotvalue = Lis[first]
    if last - first > 3:
        if pivotvalue > Lis[first + 1] and pivotvalue > Lis[first + 2]:
            if Lis[first + 1] > Lis[first + 2]:
                pivotvalue = Lis[first + 1]
            else:
                pivotvalue = Lis[first + 2]
        elif pivotvalue < Lis[first + 1] and pivotvalue < Lis[first + 2]:
            if Lis[first + 1] > Lis[first + 2]:
                pivotvalue = Lis[first + 2]
            else:
                pivotvalue = Lis[first + 1]

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
