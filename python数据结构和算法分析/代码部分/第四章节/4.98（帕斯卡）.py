N=int(input("请输入你想要帕斯卡金字塔层数：\n"))
S=[[0 for i in range(N)] for i in range(N)]
for i in range(N):
    S[i][0],S[i][i]=1,1
for i in range(N):
    for j in range(N):
        if S[i][j]!= 0:
            continue
        else:
            S[i][j]=S[i-1][j-1]+S[i-1][j]
for i in range(N):
    for j in range(N-i):
        print("   ",end="")
    for j in range(i+1):
        print("%4d" %S[i][j],end="  ")
    print("")
