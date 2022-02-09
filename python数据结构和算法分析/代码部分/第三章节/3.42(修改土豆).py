from pythonds.basic import Queue
import random


def hotPotato(namelist):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        num = random.randint(1, simqueue.size())
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


lst = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"])
print(lst)
