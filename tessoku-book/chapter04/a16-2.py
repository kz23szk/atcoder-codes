N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]
for i in range(3, N + 1):
    dp[i] = min(A[i] + dp[i - 1], B[i] + dp[i - 2])

print(dp[-1])
