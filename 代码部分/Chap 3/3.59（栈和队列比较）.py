import queue
from pythonds import Stack as Stac
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
            Tarpos = self.length - 1
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


class Stack:
    def __init__(self):
        self.Sta = UnorderedList()

    def put(self, item):
        self.Sta.append(item)

    def pop(self):
        ans = self.Sta.pop()
        return ans

    def size(self):
        return self.Sta.getLength()


class Que:
    def __init__(self):
        self.que = UnorderedList()

    def size(self):
        return self.que.getLength()

    def enqueue(self, item):
        self.que.append(item)

    def dequeue(self):
        ans = self.que.pop(1)
        return ans


S1 = Stack()
S2 = Stac()
t1 = timeit.Timer("S1.put(1000)", "from __main__ import S1")
t2 = timeit.Timer("S2.push(1000)", "from __main__ import S2")
fir_time = t1.timeit(number=10000)
sec_time = t2.timeit(number=10000)
print(fir_time, "    ", sec_time)
que1 = Que()
que2 = queue.Queue()
t3 = timeit.Timer("que1.enqueue(1000)", "from __main__ import que1")
t4 = timeit.Timer("que2.put(1000)", "from __main__ import que2")
thr_time = t3.timeit(number=10000)
for_time = t4.timeit(number=10000)
print(thr_time, "    ", for_time)
# 13.015420599999743      0.0015266000000337954
# 13.649703699999918      0.02244390000032581
"""
基于上述比较
可以明显发现手写的队列和栈都是非常慢的
建议直接使用本身库函数中包含的队列和栈
"""
