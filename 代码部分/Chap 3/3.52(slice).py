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

    def slice(self, start, stop):
        ans = []
        pos = 1
        current = self.head
        over = False
        while current is not None and not over:
            if pos >= start:
                ans.append(current.getData())
            if pos == stop - 1:
                over = True
            current = current.getNext()
            pos += 1
        return ans


Lis = UnorderedList()
for i in range(15):
    Lis.append(i)
print(Lis.slice(10, 12))
