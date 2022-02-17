"""
maxSize代表的是堆的最大容量
基本思想就是对于堆的话，加入一个值并更新
若超过最大值，则删除元素
"""

import random

maxSize = 100


class BinaryHeap:
    def __init__(self):
        self.currentSize = 0
        self.heapList = [0]

    def percUp(self, pos):
        while pos // 2:
            if self.heapList[pos] < self.heapList[pos // 2]:
                self.heapList[pos], self.heapList[pos // 2] = self.heapList[pos // 2], self.heapList[pos]
            pos //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        if self.currentSize > maxSize:
            self.heapList.pop()
            self.currentSize -= 1

    def minChild(self, pos):
        if 2 * pos + 1 > self.currentSize:
            return 2 * pos
        else:
            if self.heapList[2 * pos] < self.heapList[2 * pos + 1]:
                return 2 * pos
            else:
                return 2 * pos + 1

    def percDown(self, pos):
        while 2 * pos <= self.currentSize:
            mc = self.minChild(pos)
            if self.heapList[mc] < self.heapList[pos]:
                self.heapList[mc], self.heapList[pos] = self.heapList[pos], self.heapList[mc]
            pos = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, List):
        for item in List:
            self.insert(item)

    def getSize(self):
        return self.currentSize


Lis = [1,2,3,4,5,6,7,8,9,10]
Lis.reverse()
for i in range(10):
    newValue = random.randint(1, 50)
    # Lis.append(newValue)
print(Lis)
heap = BinaryHeap()
heap.buildHeap(Lis)
print(heap.heapList)
