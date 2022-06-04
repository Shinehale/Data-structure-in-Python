import timeit

for i in range(1,10000,1):
    t = timeit.Timer("del x[%d]" % 1, "from __main__ import x")
    x = [0 for j in range(i+1)]
    lst_time = t.timeit(number=1)
    x = {j: 1 for j in range(i+1)}
    d_time = t.timeit(number=1)
    print("the time del of the list",lst_time,"milliseconds")
    print("the time del of the dic",d_time,"milliseconds")
    # print("第 %d 次：\n lst_time = %10.3f  dt_time = %10.3f" % (i, lst_time, d_time))
"""
第一次删除结果
the time del of the list 5.999972927384079e-07 milliseconds
the time del of the dic 4.00003045797348e-07 milliseconds
最后一次删除结果
the time del of the list 2.7999994927085936e-06 milliseconds
the time del of the dic 4.999965312890708e-07 milliseconds
可以看出都是O（1）的速度
"""