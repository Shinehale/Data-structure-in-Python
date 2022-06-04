"""
算法的思想来源是快排的思想
这样获得到结果得到的平均复杂度是O(n)
但是如果是非常规整的序列或者已经排好序的序列
这样的算法的复杂度会被退化到到O(n^2)
因此快排的思想也被成为不稳定的排序
"""


import random


def calc(S, k):
    std = S[0]
    L, R = [], []
    eq = 0
    for i in range(len(S)):
        if S[i] > std:
            R.append(S[i])
        elif S[i] < std:
            L.append(S[i])
        else:
            eq += 1
    if len(L) >= k:
        calc(L, k)
    elif len(L) + eq >= k:
        global ans
        ans = std
    else:
        calc(R, k - len(L) - eq)


ans = 0
N = int(input("请输入你想要生成的随机数序列长度:"))
k = int(input("请输入你想要获得第几小元素："))
S = []
for i in range(N):
    x = random.randint(1, N)
    S.append(x)
calc(S, k)
print("您获得的随机数序列是：")
for i in range(len(S)):
    print(S[i], end=" ")
print("\n排序之后的随机数数列是：")
S.sort()
for i in range(len(S)):
    print(S[i], end=" ")
print("\n得到的第 %d 个数是：  %d" % (k, ans))
