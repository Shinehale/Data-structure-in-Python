import timeit
import sys


def calc(n):
    if n==1 or n==2:
        return 1
    else:
        return calc(n-1)+calc(n-2)


def calculate(N):
    N=N-1
    ans=[0 for i in range(N+1)]
    for i in range(N+1):
        if i==0 or i==1:
            ans[i]=1
        else:
            ans[i]=ans[i-1]+ans[i-2]
    return ans[N]


old=sys.getrecursionlimit()
sys.setrecursionlimit(100000)
t1=timeit.Timer("calc(35)","from __main__ import calc")
t2=timeit.Timer("calculate(35)","from __main__ import calculate")
fir_time=t1.timeit(number=1)
sec_time=t2.timeit(number=1)
print(fir_time,sec_time)
# >> 3.080608199999915 1.44999999065476e-05
"""
从计算35阶乘可以明显看出递归有着明显的时间和空间上的劣势
无法很好的处理问题
"""