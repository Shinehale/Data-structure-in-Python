def calc(a, b, ls):
    if a < b:
        a, b = b, a
    p1 = a % b
    p2 = b - p1
    if p1 == ls % b:
        k = (ls % b) // p1
        ans = a // b - k
        print("将容量大的桶装满\n再向容量小的桶倒满，并且将容量小的的倒空\n重复上述操作 %d 次\n最终容量大的桶剩下的就是所求" % ans)
    elif p2 == ls % b:
        k = (ls % b) // p2
        ans = (ls + a) // b
        print("将容量小的装满，并且向容量大的倒，重复 %d 次 \n若容量大的桶满了，则将其倒空\n最终大桶中的剩下便是所求" % ans)
    else:
        print("暂且无法通过这两个桶完成你想要的剩余\n")


a, b = 3, 4
las = 2
calc(a, b, las)
