import queue
from pythonds.basic import Stack


def addEdge(x, y):
    G[x].append(y)


def paint(x):
    global num
    S.pop()
    color[x] = num
    vis[x] = False


def Tarjan(x):
    global index
    index += 1
    dfn[x] = low[x] = index
    vis[x] = True
    S.push(x)
    for y in G[x]:
        if not dfn[y]:
            Tarjan(y)
            low[x] = min(low[x], low[y])
        elif vis[y]:
            low[x] = min(low[x], dfn[y])
    if dfn[x] == low[x]:
        global num
        num += 1
        while S.peek() != x:
            t = S.peek()
            paint(t)
        paint(x)


G = {}
R = list(map(int, input().split()))
N, M = R[0], R[1]
for i in range(N):
    G[i] = []
for i in range(M):
    R = list(map(int, input().split()))
    addEdge(R[0]-1, R[1]-1)
dfn, low, vis, color = [0] * N, [0] * N, [False] * N, [0] * N
S = Stack()
index = 0
num = 0
for i in range(N):
    if not dfn[i]:
        Tarjan(i)
for i in range(N):
    print(color[i],end=" ")
"""
输入样例：
7 11
1 2
2 4 
4 1
2 3
3 5
5 6
3 7
7 5
6 7
2 5
4 6
输出：
3 3 2 3 1 1 1 
"""
