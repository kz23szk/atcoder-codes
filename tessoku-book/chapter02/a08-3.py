from itertools import accumulate

H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
c_sum = [[0] * (W + 1)]
# w方向の累積和を計算する
for x in X:
    c_sum.append([0] + list(accumulate(x)))

# h方向の累積和を計算する
for w in range(W + 1):
    for h in range(2, H + 1):
        c_sum[h][w] += c_sum[h - 1][w]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(c_sum[C][D] - c_sum[C][B - 1] - c_sum[A - 1][D] + c_sum[A - 1][B - 1])
