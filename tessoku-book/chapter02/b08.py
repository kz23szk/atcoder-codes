N = int(input())
max_index = 1501
c_sum = [[0 for _ in range(max_index)] for _ in range(max_index)]
for _ in range(N):
    x, y = map(int, input().split())
    c_sum[y][x] += 1

# x方向の累積和を取る
for y in range(1, max_index):
    for x in range(1, max_index):
        c_sum[y][x] += c_sum[y][x - 1]

# y方向の累積和を取る
for x in range(1, max_index):
    for y in range(1, max_index):
        c_sum[y][x] += c_sum[y - 1][x]

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    print(c_sum[y2][x2] - c_sum[y2][x1 - 1] - c_sum[y1 - 1][x2] + c_sum[y1 - 1][x1 - 1])
