N, W = map(int, input().split())
wv = [tuple()] + [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(W + 1):
        weight, value = wv[i]
        # ここは重さが足りないのでそのままスライド
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        # 重さが足りているので前回の選択か今回の重さを選択したときの価値の大きい方で更新
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(max(dp[N]))
