N = int(input())
max_index = 1501
cells = [[0 for _ in range(max_index)] for _ in range(max_index)]
for _ in range(N):
    w1, h1, w2, h2 = map(int, input().split())
    cells[h1][w1] += 1
    cells[h1][w2] -= 1
    cells[h2][w1] -= 1
    cells[h2][w2] += 1

for h in range(max_index):
    for w in range(1, max_index):
        cells[h][w] += cells[h][w - 1]

for w in range(max_index):
    for h in range(1, max_index):
        cells[h][w] += cells[h - 1][w]

count = 0
for h in range(max_index):
    for w in range(max_index):
        if cells[h][w] > 0:
            count += 1
print(count)
