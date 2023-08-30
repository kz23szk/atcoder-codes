# CPythonではTLEでPyPyでは通る
N = int(input())
INF = 10 ** 11
X, Y, Z = [0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    X[i], Y[i], Z[i] = map(int, input().split())

z_sum = sum(Z)
dp = [INF for _ in range(z_sum + 1)]
dp[0] = 0

for i in range(N):
    # Z[i] 議席獲得するのに必要な鞍替え人数
    w = (Y[i] - X[i]) // 2 + 1 if Y[i] > X[i] else 0

    for j in range(Z[i], z_sum + 1)[::-1]:
        dp[j] = min(dp[j], dp[j - Z[i]] + w if dp[j - Z[i]] != INF else INF)

kahansu = z_sum // 2 + 1
print(min(dp[kahansu:]))
