H, W, N = map(int, input().split())
c_sum = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    c_sum[A][B] += 1
    c_sum[C + 1][B] -= 1
    c_sum[A][D + 1] -= 1
    c_sum[C + 1][D + 1] += 1

# W方向の累積和を計算する
for h in range(1, H + 2):
    for w in range(1, W + 2):
        c_sum[h][w] += c_sum[h][w - 1]

# H方向の累積和を計算する
for w in range(1, W + 2):
    for h in range(1, H + 2):
        c_sum[h][w] += c_sum[h - 1][w]

for row in c_sum[1:-1]:
    print(*row[1:W + 1])
