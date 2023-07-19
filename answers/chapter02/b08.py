N = int(input())
max_index = 1501
counts = [[0 for _ in range(max_index)] for _ in range(max_index)]

for _ in range(N):
    x, y = map(int, input().split())
    counts[x][y] += 1

# 横方向の累積和を取る
for h in range(1, max_index):
    for w in range(1, max_index):
        counts[h][w] += counts[h][w - 1]

# 縦方向の累積和を取る
for w in range(max_index):
    for h in range(1, max_index):
        counts[h][w] += counts[h - 1][w]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(counts[c][d] - counts[c][b - 1] - counts[a - 1][d] + counts[a - 1][b - 1])
