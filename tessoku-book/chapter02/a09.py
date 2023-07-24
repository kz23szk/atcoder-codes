import itertools

H, W, N = map(int, input().split())
counts = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    counts[a][b] += 1
    counts[c + 1][b] -= 1
    counts[a][d + 1] -= 1
    counts[c + 1][d + 1] += 1

# 横方向の累積和を計算
for h in range(H + 1):
    counts[h] = list(itertools.accumulate(counts[h]))

# 縦方向の累積和を計算
for w in range(W + 1):
    for h in range(1, H + 1):
        counts[h][w] += counts[h - 1][w]

# 答えを整形して出力
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if w >= 2:
            print(" ", end="")
        print(counts[h][w], end="")
    print()
