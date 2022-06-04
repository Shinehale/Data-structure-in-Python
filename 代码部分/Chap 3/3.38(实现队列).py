"""
列表末端是队尾
"""


class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



que=Queue()
que.enqueue(45)
print(que.isEmpty())
