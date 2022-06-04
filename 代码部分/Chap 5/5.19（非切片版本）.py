import timeit

N = 10000000
S = [i * 2 + 1 for i in range(N)]


def binarySearch1(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def binarySearch(L, R, item):
    if L > R:
        return False
    else:
        mid = (L + R) // 2
        if S[mid] == item:
            return True
        else:
            if item < S[mid]:
                return binarySearch(L, mid - 1, item)
            else:
                return binarySearch(mid + 1, R, item)


t1 = timeit.Timer("binarySearch1(S,2*N-1)", "from __main__ import binarySearch1,N,S")
t2 = timeit.Timer("binarySearch(0,2*N-1,2*N-1)", "from __main__ import binarySearch,N,S")
fir_time = t1.timeit(number=10)
sec_time = t2.timeit(number=10)
print("when N is %d : %lf %lf" % (N, fir_time, sec_time))
# >> when N is 10000 : 0.000057 0.000008
# >> when N is 100000 : 0.000079 0.000008
# >> when N is 1000000 : 0.000093 0.000008
# >> when N is 10000000 : 0.000056 0.000005
"""
在非切片版本中
因为少了切片的时间
所以大幅提高了时间运行速度
"""
