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


class OrderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def getLength(self):
        return self.length

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() >= item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.length += 1

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            return "".join("not found the data")

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length = -1
        return "".join("the data has been removed!")


Lis = OrderedList()
for i in range(15):
    Lis.add(i)
for i in range(15):
    Lis.add(i)
ans1 = Lis.remove(14)
ans2 = Lis.remove(14)
ans3 = Lis.remove(14)
print(ans1, " ", ans2, " ", ans3)
# >> the data has been removed!
# the data has been removed!
# not found the data
