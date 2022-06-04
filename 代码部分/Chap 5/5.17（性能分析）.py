import timeit


def binarySearch(L, R, item):
    if L == R:
        return L
    mid = (L + R) // 2
    if S1[mid] == item:
        return mid
    elif S1[mid] < item:
        return binarySearch(mid + 1, R, item)
    else:
        return binarySearch(L, mid, item)


def find1(item):
    pos = 0
    while S1[pos] < item:
        pos += 1
    return pos


def find2(item):
    pos = binarySearch(0, 10000, item)
    return pos


S1 = [i ** 1.2 for i in range(10000)]
t1 = timeit.Timer("find1(60000)", "from __main__ import S1,find1")
t2 = timeit.Timer("find2(60000)", "from __main__ import S1,find2")
fir_time = t1.timeit(number=1000)
sec_time = t2.timeit(number=1000)
print(fir_time)
print(sec_time)
# >>1.165027499999269
# >>0.004411100002471358
"""
从结果中不难看出，在有序列表中进行折半搜索
速度明显高于单纯的逐个搜索
"""