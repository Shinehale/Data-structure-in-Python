import timeit

ls1=[i for i in range(1000)]
ls2=[i for i in range(10000)]
# 产生两个不同n大小的列表
def test1(value):
    ans=ls1[value]
    return ans

def test2(value):
    ans=ls2[value]
    return ans

t1=timeit.Timer("test1(500)","from __main__ import test1")
t2=timeit.Timer("test2(500)","from __main__ import test2")
print("index of ls1 ",t1.timeit(number=10000),"milliseconds")
print("index of ls2 ",t2.timeit(number=10000),"milliseconds")
"""
>> index of ls1  0.001014900000882335 milliseconds
>> index of ls2  0.0010357000028307084 milliseconds
从输出结果发现，时间差别并没有因为列表长度的增加而有明显增加
说明索引操作的时间复杂度单次就是O(1)
"""