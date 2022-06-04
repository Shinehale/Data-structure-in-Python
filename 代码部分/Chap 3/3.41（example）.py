"""
考虑这样一个问题：
    排队等待洗车
    我们首先需要定义一个类（Task）表示单个洗车任务
    单个洗车任务所需要的时间：设置成1-60内随机整数来表示60分钟内洗好
"""
import random
from queue import Queue as Que


class Task:

    def __init__(self, num):
        self.time = random.randint(1, 60)
        self.index = num

    def getTime(self):
        return self.time


N = int(input("请输入你想要产生的任务总数量:\n"))
que = Que()
for i in range(N):
    new_ = Task(i)
    que.put(new_)
time=0
lef=0
while not que.empty():
    now=que.get()
    while True:
        time+=1
        lef+=1
        if lef==now.getTime():
            break
    lef=0
print("The total time of the queue is {:d}".format(time))


