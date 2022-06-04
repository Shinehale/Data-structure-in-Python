import random
import timeit
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1

    def getLength(self):
        return self.length

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    def append(self, item):
        current = self.head
        if self.head is None:
            newNode = Node(item)
            self.head = newNode
            self.length += 1
            return

        while current.getNext() is not None:
            current = current.getNext()
        newNode = Node(item)
        current.setNext(newNode)
        self.length += 1

    def index(self, item):
        current = self.head
        pos = 1
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if current is None:
            return "not found"
        else:
            return pos

    def insert(self, Tarpos, item):
        current = self.head
        pos = 1
        found = False
        while current is not None and not found:
            if pos == Tarpos:
                found = True
                newNode = Node(item)
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1
            else:
                current = current.getNext()
                pos += 1

    def pop(self, Tarpos=-1):
        if Tarpos == -1:
            Tarpos = self.length-1
        current = self.head
        previous = None
        found = False
        pos = 1
        while current is not None and not found:
            if pos == Tarpos:
                found = True
            previous = current
            current = current.getNext()

            pos += 1
        if previous is None:
            self.head = None
        else:
            previous.setNext(current.getNext())
        self.length -= 1
        return current.getData()


Lis1=[]
Lis2=UnorderedList()
for i in range(15):
    newValue=random.randint(1,60)
    Lis1.append(newValue)
    Lis2.append(newValue)
t1=timeit.Timer("Lis1.append(100)","from __main__ import Lis1")
t2=timeit.Timer("Lis2.append(100)","from __main__ import Lis2")
fir_time=t1.timeit(number=10000)
sec_time=t2.timeit(number=10000)
print(fir_time,"  ",sec_time)
# >> 0.002300199999808683    13.010699000000386
"""
通过上述比较可以明显看出来，手写的链表实现的列表
运行速度是非常慢的
"""