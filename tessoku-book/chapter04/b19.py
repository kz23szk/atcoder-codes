import sys

N, W = map(int, input().split())
w, v = [0 for i in range(N + 1)], [0 for i in range(N + 1)]
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

MAX_VALUE = 1000 * 100
MAX_WEIGHT = 10 ** 9 + 1
dp = [[MAX_WEIGHT for i in range(MAX_VALUE + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(MAX_VALUE + 1):
        if j - v[i] < 0 or dp[i - 1][j - v[i]] + w[i] > W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])

for v in range(MAX_VALUE + 1)[::-1]:
    if dp[-1][v] <= W:
        print(v)
        sys.exit(0)
