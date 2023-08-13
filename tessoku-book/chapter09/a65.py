N = int(input())
A = [0, 0] + list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]
for i in range(2, N + 1)[::-1]:
    dp[A[i]] += dp[i] + 1

print(*dp[1:])
