import itertools

N = int(input())
max_index = 1500
counts = [[0 for _ in range(max_index + 1)] for _ in range(max_index + 1)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    counts[a][b] += 1
    counts[a][d] -= 1
    counts[c][b] -= 1
    counts[c][d] += 1

for h in range(max_index + 1):
    counts[h] = list(itertools.accumulate(counts[h]))

for w in range(max_index + 1):
    for h in range(1, max_index + 1):
        counts[h][w] += counts[h - 1][w]

# 累積和を見やすく整形して出力
# for h in range(max_index + 1):
#     for w in range(max_index + 1):
#         if w >= 2:
#             print(" ", end="")
#         print(counts[h][w], end="")
#     print()

cnt = 0
for h in range(max_index + 1):
    for w in range(max_index + 1):
        cnt += 1 if counts[h][w] > 0 else 0

print(cnt)
