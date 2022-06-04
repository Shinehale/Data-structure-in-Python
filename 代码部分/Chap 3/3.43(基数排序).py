"""
基数排序：
当前版本难以处理负数
因此排序过程需要保证录入的数据都是正整数
"""

import queue


def solve(Bit):
    while M_bar.qsize():
        now = M_bar.get()
        backup = now
        for i in range(Bit):
            now //= 10
        now = now % 10
        D_bar[now].put(backup)
    for i in range(10):
        while D_bar[i].qsize():
            M_bar.put(D_bar[i].get())


M_bar = queue.Queue()
D_bar = []
for i in range(10):
    D_bar.append(queue.Queue())
N = int(input("请输入你想要排序的数的个数：\n"))
R = list(map(int, input().split()))
maxValue = 0
for i in range(N):
    M_bar.put(R[i])
    maxValue = max(maxValue, R[i])
bits = 0
while maxValue > 0:
    bits += 1
    maxValue //= 10
for bit in range(bits):
    solve(bit)
ans = []
while M_bar.qsize():
    ans.append(M_bar.get())
print(ans)
