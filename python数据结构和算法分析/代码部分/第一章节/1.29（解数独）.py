"""
显然数独的解并不唯一，那么本程序只能输出一个可行解
如果想要输出所有可行解。那么只需要在最终dfs截至条件中选择写入
return 来代替exit(0)即可
已经证明。解数独是NP问题
现如今没办法使用有限步数内的推理而得到最终结果
只有搜素才能解决出来
输入样例：
_ _ _ _ _ _ _ _ _
_ 1 2 _ _ 6 _ 9 _
_ _ _ 2 5 _ _ _ 1
_ _ 8 1 _ _ _ 4 _
_ _ 5 _ 7 _ 3 _ _
_ 4 _ _ _ 2 9 _ _
2 _ _ _ 3 4 _ 7 _
_ 7 _ 9 _ _ 6 5 _
_ _ _ _ _ _ _ _ _
输出样例：
3 5 4 8 9 1 7 2 6
8 1 2 7 4 6 5 9 3
6 9 7 2 5 3 4 8 1
9 3 8 1 6 5 2 4 7
1 2 5 4 7 9 3 6 8
7 4 6 3 8 2 9 1 5
2 6 1 5 3 4 8 7 9
4 7 3 9 1 8 6 5 2
5 8 9 6 2 7 1 3 4
"""
import copy


def check(pos, value):
    i, j = ls[pos][0], ls[pos][1]
    new_ = set()
    for x in range(9):
        if ans[i][x] not in new_:
            new_.add(ans[i][x])
        if ans[x][j] not in new_:
            new_.add(ans[x][j])
    Pi, Pj = i // 3, j // 3
    for x in range(3):
        for y in range(3):
            if ans[Pi * 3 + x][Pj * 3 + y] not in new_:
                new_.add(ans[Pi * 3 + x][Pj * 3 + y])
    if value not in new_:
        return True
    else:
        return False


def calc(pos):
    if pos == tot:
        for i in range(9):
            for j in range(9):
                print(ans[i][j], end=" ")
            print("")
        exit(0)
    for i in range(9):
        if check(pos, i + 1):
            ans[ls[pos][0]][ls[pos][1]] = i + 1
            if calc(pos + 1): return True
            ans[ls[pos][0]][ls[pos][1]] = 0


print("请输入你想要解答的数独，一行中相邻两个数字之间用空格隔开，若等待求解则用_表示")
s = [[] for i in range(9)]
for i in range(9):
    R = input().split()
    for x in R:
        if x == '_':
            s[i].append(0)
        else:
            s[i].append(int(x))
ans = copy.deepcopy(s)
tot = 0
ls = []
for i in range(9):
    for j in range(9):
        if ans[i][j] == 0:
            tot += 1
            ls.append((i, j))
calc(0)
