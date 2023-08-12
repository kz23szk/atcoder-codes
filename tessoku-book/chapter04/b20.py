S = list(input())
T = list(input())

# 最長部分文字列を求める
dp = [ [0 for _ in range(len(S)+1)] for _ in range(len(T)+1)]

for i in range(1, len(T) + 1):
    for j in range(1, len(S) + 1):
        if T[i-1] == S[j-1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for row in dp:
    print(*row)