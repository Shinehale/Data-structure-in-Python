import queue


def BFS(x, y):
    que = queue.Queue()
    vis = [[False for i in range(m)] for j in range(n)]
    vis[x][y]=True
    newone = (x, y, "(" + str(x+1) + "," + str(y+1) + ")")
    que.put(newone)
    while not que.empty():
        item = que.get()
        x, y, string = item[0], item[1], item[2]
        for each in turn:
            newX = x + each[0]
            newY = y + each[1]
            if newX >= n or newX < 0 or newY >= m or newY < 0:
                continue
            if mp[newX][newY] == 0:
                continue
            if vis[newX][newY]:
                continue
            newString = string + "->(" + str(newX+1) + "," + str(newY+1) + ")"
            newOne = (newX, newY, newString)
            if newX == s - 1 and newY == t - 1:
                print(newString)
            else:
                vis[newX][newY]=True
                que.put(newOne)


R = list(map(int, input().split()))
n, m = R[0], R[1]
mp = []
turn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(n):
    R = list(map(int, input().split()))
    mp.append(R)
R = list(map(int, input().split()))
x, y = R[0], R[1]
R = list(map(int, input().split()))
s, t = R[0], R[1]
BFS(x - 1, y - 1)
"""
输入样例：
5 6
1 0 0 1 0 1
1 1 1 0 1 1
0 0 1 0 1 0
1 1 1 1 1 0
1 1 1 0 1 1
1 1
5 6
输出样例：
(1,1)->(2,1)->(2,2)->(2,3)->(3,3)->(4,3)->(4,4)->(4,5)->(5,5)->(5,6)
"""