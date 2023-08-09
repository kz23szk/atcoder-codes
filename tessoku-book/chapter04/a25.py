H, W = map(int, input().split())
cells = [list(input()) for _ in range(H)]
dp = [[0 for i in range(W)] for j in range(H)]

# 一番上の行を初期化
for i, cell in enumerate(cells[0]):
    if cell == "#":
        break
    dp[0][i] = 1

# 一番左の列を初期化
for h in range(H):
    if cells[h][0] == "#":
        break
    dp[h][0] = 1

for h in range(1, H):
    for w in range(1, W):
        if cells[h][w] == '.':
            dp[h][w] = dp[h - 1][w] + dp[h][w - 1]

print(dp[-1][-1])
