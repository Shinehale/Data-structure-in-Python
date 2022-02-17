"""
算法复杂度：
O(n log n)
"""
import random


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
        self.heapList = [0] + List[:]
        self.currentSize = len(List)
        pos = self.currentSize // 2
        while pos:
            self.percDown(pos)
            pos -= 1

    def getSize(self):
        return self.currentSize


Lis = []
for i in range(15):
    newValue = random.randint(1, 1500)
    Lis.append(newValue)
print(Lis)
H = BinaryHeap()
H.buildHeap(Lis)
ans=[]
while H.getSize():
    ans.append(H.delMin())
print(ans)

