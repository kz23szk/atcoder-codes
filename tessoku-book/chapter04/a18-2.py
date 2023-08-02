N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    for j in range(S + 1):
        if dp[i-1][j] or (j-A[i] >= 0 and dp[i-1][j-A[i]]):
            dp[i][j] = True

if dp[-1][-1]:
    print("Yes")
else:
    print("No")
