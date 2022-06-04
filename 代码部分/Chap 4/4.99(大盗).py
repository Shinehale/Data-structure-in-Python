ans = [[0 for i in range(21)] for j in range(6)]
w = [2, 3, 4, 5, 9]
v = [3, 4, 8, 8, 10]
for i in range(5):
    for j in range(21):
        # 状态转移方程
        ans[i + 1][j] = ans[i][j]
        if j - w[i] >= 0:
            ans[i + 1][j] = max(ans[i][j - w[i]] + v[i], ans[i + 1][j])
Ans = 0
for i in range(21):
    Ans = max(Ans, ans[5][i])
print(ans[5][20])
