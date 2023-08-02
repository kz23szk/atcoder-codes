S = input()
T = input()

dp = [[0 for _ in range(len(S) + 1)] for _ in range(len(T) + 1)]

for i, t in enumerate(T):
    for j, s in enumerate(S):
        if s == t:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + 1)
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])
