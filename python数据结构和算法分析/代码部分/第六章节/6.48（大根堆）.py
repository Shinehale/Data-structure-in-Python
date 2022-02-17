"""
堆的本质就是只管堆顶元素的值
而不管堆内元素在同一层级中是否有序
但是必须保证根节点要比子节点优先级高
"""
import random


class BinaryHeap:
    def __init__(self):
        self.currentSize = 0
        self.heapList = [0]

    def percup(self, pos):
        while pos // 2:
            if self.heapList[pos] > self.heapList[pos // 2]:
                self.heapList[pos], self.heapList[pos // 2] = self.heapList[pos // 2], self.heapList[pos]
            pos //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percup(self.currentSize)

    def maxChild(self, pos):
        if 2 * pos + 1 > self.currentSize:
            return 2 * pos
        else:
            if self.heapList[2 * pos] > self.heapList[2 * pos + 1]:
                return 2 * pos
            else:
                return 2 * pos + 1

    def percDown(self, pos):
        while 2 * pos <= self.currentSize:
            mc = self.maxChild(pos)
            if self.heapList[mc] > self.heapList[pos]:
                self.heapList[mc], self.heapList[pos] = self.heapList[pos], self.heapList[mc]
            pos = mc

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, Lis):
        self.heapList = [0] + Lis[:]
        self.currentSize = len(Lis)
        pos = self.currentSize // 2
        while pos:
            self.percDown(pos)
            pos -= 1


Lis = []
for i in range(8):
    newValue = random.randint(1, 50)
    Lis.append(newValue)
print(Lis)
H = BinaryHeap()
H.buildHeap(Lis)
ans = H.delMax()
print(ans)
