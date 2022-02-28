"""
本题目数据直接由程序生成并且
完成了题目要求的对于有向图的反向
"""

import random


class Graph:
    def __init__(self, n):
        self.size = n
        self.G = {}
        for i in range(n):
            self.G[i] = []
        self.vised = [False] * n
        self.depth = [0] * n

    def addEdge(self, x, y, z):
        pos = self.G[x]
        pos.append((y, z))

    def transpose(self):
        N = self.size
        newG = Graph(N)
        for i in range(self.size):
            lis = self.G[i]
            for item in lis:
                y, z = item[0], item[1]
                newG.addEdge(y, i, z)
        self.G = newG.G


n = random.randint(10, 15)
m = random.randint(3 * n, 4 * n)
Gra = Graph(n)
for i in range(m):
    x, y, z = random.randint(1, n), random.randint(1, n), random.randint(50, 100)
    if x == y:
        continue
    Gra.addEdge(x - 1, y - 1, z)
for i in range(n):
    print(i + 1, end=" :")
    for item in Gra.G[i]:
        print(item[0] + 1, end=" ")
    print("")
print("_________")
Gra.transpose()
for i in range(n):
    print(i + 1, end=" :")
    for item in Gra.G[i]:
        print(item[0] + 1, end=" ")
    print("")
