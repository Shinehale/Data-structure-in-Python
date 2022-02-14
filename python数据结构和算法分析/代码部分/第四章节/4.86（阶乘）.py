def calc(n):
    if n == 1:
        return 1
    elif n <= 0:
        return "There must be something wrong!"
    return n * calc(n - 1)


N = int(input("请输入你想要计算的阶乘：\n"))
ans = calc(N)
print(ans)
