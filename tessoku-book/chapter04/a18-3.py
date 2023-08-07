N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(S+1):
        if j - A[i] >= 0:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]
        else:
            dp[i][j] = dp[i-1][j]
print("Yes") if dp[-1][-1] else print("No")
