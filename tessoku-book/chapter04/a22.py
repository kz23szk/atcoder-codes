N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

dp = [0 for i in range(N+1)]
for i in range(1, N):
    dp[A[i]] = max(dp[i] + 100, dp[A[i]])
    dp[B[i]] = max(dp[i] + 150, dp[B[i]])

print(dp[N])
