import timeit
dt1={}
dt2={}
for i in range(1000):
    dt1[i]=i
for j in range(10000):
    dt2[j]=j

for i in range(1000):
    t1=timeit.Timer("dt1[%d]" % i ,"from __main__ import dt1,i")
    t2=timeit.Timer("dt2[%d]" % i ,"from __main__ import dt2,i")
    print("value of dt1[]",t1.timeit(number=1000),"milliseconds")
    print("value of dt2[]",t2.timeit(number=1000),"milliseconds")

"""
第一次时：
value of dt1[] 5.230000169831328e-05 milliseconds
value of dt2[] 5.32000012753997e-05 milliseconds
最后一次时：
value of dt1[] 6.760000178474002e-05 milliseconds
value of dt2[] 6.529999882332049e-05 milliseconds
第一次跟最后一次时间相差不大，并且每次的两个不同长度列表所需时间
没有明显的增加
这样变相说明了字典取值的操作是用来O(1)
"""