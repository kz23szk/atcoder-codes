import itertools

H, W = map(int, input().split())
cell = [[0] * (W + 1)]
# 横方向の累積和を計算
for i in range(H):
    cell.append([0] + list(itertools.accumulate(list(map(int, input().split())))))

# 縦方向の累積和を計算
for i in range(1, W + 1):
    for j in range(1, H + 1):
        cell[j][i] += cell[j - 1][i]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(cell[c][d] - cell[c][b - 1] - cell[a - 1][d] + cell[a - 1][b - 1])
