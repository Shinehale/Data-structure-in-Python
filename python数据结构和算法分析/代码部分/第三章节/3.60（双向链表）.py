import random


class Node:
    def __init__(self, item):
        self.next = None
        self.data = item
        self.back = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def getBack(self):
        return self.back

    def setNext(self, tarNext):
        self.next = tarNext
        tarNext.back = self


class DoubleLinkedList:
    def __init__(self):
        self.headNode = Node("0")
        self.length = 0

    def add(self, item):
        newNode = Node(item)
        if self.length == 0:
            self.headNode.setNext(newNode)
            newNode.setNext(self.headNode)
        else:
            newNode.setNext(self.headNode.getNext())
            self.headNode.setNext(newNode)
        self.length += 1

    def getLength(self):
        return self.length

    def search(self, item):
        current = self.headNode.getNext()
        found = False
        while current != self.headNode and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found


Lis = DoubleLinkedList()
lastValue = 0
for i in range(15):
    newValue = random.randint(1, 60)
    Lis.add(newValue)
    if i==0:
        lastValue = newValue
ans = Lis.search(lastValue)
print(ans)
