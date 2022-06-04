"""
利用列表和L，R来实现对队首元素的定位
以及一些操作
"""


class Queue:
    def __init__(self):
        self.items = []
        self.L = 0
        self.R = -1

    def dequeue(self):
        num = self.items[self.L]
        self.L += 1
        return num

    def enqueue(self, item):
        self.R += 1
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


que = Queue()
que.enqueue(15)
print(que.dequeue())
