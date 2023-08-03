N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False for i in range(S + 1)] for j in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    for j in range(S + 1):
        # 選ばない
        dp[i][j] = dp[i - 1][j]
        # 選ぶ
        if j - A[i] >= 0:
            dp[i][j] = dp[i - 1][j - A[i]] or dp[i - 1][j]

if dp[-1][-1]:
    print("Yes")
else:
    print("No")
