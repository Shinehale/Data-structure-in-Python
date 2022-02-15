import re

INF = 2147483647


def calc(str1, str2):
    leng1, leng2 = len(str1), len(str2)
    dp = [[INF for i in range(leng2 + 1)] for j in range(leng1 + 1)]
    dp[0][0] = 0
    for i in range(1, leng1 + 1, 1):
        dp[i][0] = i
    for j in range(1, leng2 + 1, 1):
        dp[0][j] = j
    for i in range(1, leng1 + 1, 1):
        for j in range(1, leng2 + 1, 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 5)
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 20)
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 20)
    return dp[leng1][leng2]


m1 = r"\"([a-z]*)\""
m2 = r"\"([a-z]*)\""
R = input()
s1 = re.findall(m1, R)[0]
R = input()
s2 = re.findall(m2, R)[0]
ans = calc(s1, s2)
print(ans)
"""
输入示例:
"intention"
"execution"
输出示例:
25
"""
