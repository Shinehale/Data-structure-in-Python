import queue


def addEdge(x, y, z):
    if x not in G:
        G[x] = []
    if y not in G:
        G[y] = []
    G[x].append((y, z))
    deg[y] += 1


def topSort(G):
    vised = [False] * n
    que = queue.Queue()
    ans = []
    for i in range(n):
        if deg[i] == 0:
            que.put(i)
    while que.qsize():
        x = que.get()
        vised[x] = True
        ans.append(x)
        for item in G[x]:
            y = item[0]
            if not vised[y]:
                deg[y] -= 1
                if deg[y] == 0:
                    que.put(y)
    print(ans)


G = {}
R = list(map(int, input().split()))
n, m = R[0], R[1]
deg = [0] * n
for i in range(m):
    R = list(map(int, input().split()))
    x, y = R[0], R[1]
    addEdge(x, y, 0)
topSort(G)

"""
输入样例：
6 6
4 0
4 1
5 0
5 2
2 3
3 1
输出：
4,5,0,2,3,1
"""
