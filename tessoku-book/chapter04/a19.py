N, W = map(int, input().split())
w, v = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    w[i], v[i] = map(int, input().split())

# 1次元でもいける？
dp = [0 for i in range(W + 1)]

for i in range(N):
    for j in range(W + 1)[::-1]:
        if j - w[i] >= 0:
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(max(dp))
