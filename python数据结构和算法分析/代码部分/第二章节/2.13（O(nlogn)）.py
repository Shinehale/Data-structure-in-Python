"""
python内置的排序算法可以做到O(nlogn)
这样的复杂度
直接排序之后再直接第k小
这样得到的复杂度是O(nlogn)
"""

import random

ans = 0
N = int(input("请输入你想要生成的随机数序列长度:"))
k = int(input("请输入你想要获得第几小元素："))
S = []
for i in range(N):
    x = random.randint(1, N)
    S.append(x)
S.sort()
ans = S[k - 1]
print("您获得的随机数序列是：")
for i in range(len(S)):
    print(S[i], end=" ")
print("\n得到的第 %d 个数是：  %d" % (k, ans))
