import itertools

H, W = map(int, input().split())
cells = [[0] * (W + 1)]
for h in range(H):
    row = [0] + list(map(int, input().split()))
    cells.append(row)

c_sums = [[0] * (W + 1)]
# 列方向の累積を計算
for h in range(1, H + 1):
    c_sums.append(list(itertools.accumulate(cells[h])))

for w in range(1, W + 1):
    for h in range(1, H + 1):
        c_sums[h][w] += c_sums[h - 1][w]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    total = c_sums[c][d] - c_sums[c][b - 1] - c_sums[a - 1][d] + c_sums[a - 1][b - 1]
    print(total)
