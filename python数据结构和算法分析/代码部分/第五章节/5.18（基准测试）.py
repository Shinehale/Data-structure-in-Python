import timeit

N = 1000000
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


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid + 1:], item)


t1 = timeit.Timer("binarySearch1(S,2*N-1)", "from __main__ import binarySearch1,N,S")
t2 = timeit.Timer("binarySearch(S,2*N-1)", "from __main__ import binarySearch,N,S")
fir_time = t1.timeit(number=10)
sec_time = t2.timeit(number=10)
print("when N is %d : %lf %lf" % (N, fir_time, sec_time))
# >> when N is 10000: 0.000032 0.000369
# >> when N is 100000 : 0.000073 0.012874
# >> when N is 1000000 : 0.000047 0.185749
"""
随着N的增大
明显看出递归的时间增加但是非递归版本的程序
所需要的时间并没有明显增加
从而证明对列表切片需要大量时间
"""
