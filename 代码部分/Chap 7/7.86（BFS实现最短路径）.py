import queue

INF = 2**31-1


class Graph:
    def __init__(self, n):
        self.G = {}
        self.size = n
        for i in range(n):
            self.G[i] = []
        self.vised = [False] * n

    def addEdge(self, x, y, z):
        self.G[x].append((y, z))


def SPFA(pos):
    dis[pos] = 0
    que = queue.Queue()
    que.put(pos)
    Gra.vised[pos] = True
    while not que.empty():
        x = que.get()
        Gra.vised[x]=False
        for item in Gra.G[x]:
            y, z = item[0], item[1]
            if dis[y] > dis[x] + z:
                dis[y] = dis[x] + z
                if not Gra.vised[y]:
                    Gra.vised[y] = True
                    que.put(y)


R = list(map(int, input().split()))
n, m, s, t = R[0], R[1], R[2], R[3]
Gra = Graph(n)
for i in range(m):
    R = list(map(int, input().split()))
    x, y, z = R[0]-1, R[1]-1, R[2]
    Gra.addEdge(x, y, z)
    Gra.addEdge(y,x,z)
dis = [INF] * n
SPFA(s-1)
print(dis[t-1])
"""
输入样例：
10 20 9 4
5 6 308
8 10 696
4 2 569
8 6 471
1 2 874
5 3 130
4 5 804
8 9 89
10 4 717
10 9 41
7 6 998
1 6 639
7 9 650
7 8 339
3 1 597
9 1 622
7 10 2
5 1 4
1 4 372
1 10 163
输出样例：
576
"""