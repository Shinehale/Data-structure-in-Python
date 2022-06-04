import heapq
import random


class PriorityQueue:
    def __init__(self):
        self.Lis = []

    def enqueue(self, value):
        heapq.heappush(self.Lis, value)

    def dequeue(self):
        retval = heapq.heappop(self.Lis)
        return retval


que = PriorityQueue()
for i in range(20):
    newValue = random.randint(1, 10000)
    que.enqueue(newValue)
    print(newValue, end=" ")
ans = que.dequeue()
print("\n", ans)
