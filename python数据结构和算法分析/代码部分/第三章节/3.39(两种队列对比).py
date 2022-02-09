import timeit
class Queue_fir:
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

class Queue_sec:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

que1=Queue_fir()
que2=Queue_sec()
for i in range(1000):
    que1.enqueue(i)
    que2.enqueue(i)
t1=timeit.Timer("que1.enqueue(1000)", "from __main__ import que1")
fir_time=t1.timeit(number=10000)
t2=timeit.Timer("que2.enqueue(1000)", "from __main__ import que2")
sec_time=t2.timeit(number=10000)
print(fir_time," ",sec_time)
# >> 0.002802300004987046   0.026987200006260537
"""
当运行次数为10000时，明显第二种队列增加数字时间要明显增加，相差10倍
我们可以发现在这样情况下，一定会导致时间上明显的延迟
"""