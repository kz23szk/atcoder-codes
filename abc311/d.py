N, M = map(int, input().split())
cells = []
for _ in range(N):
    cell = [0 if s == "#" else 1 for s in list(input())]
    cells.append(cell)

for c in cells:
    print(c)

# つきあたりの点を保持していって、移動できるつきあたりがどちらも保持されていたら終了
tukiatari = [(1,1)]
x, y = 1,1
while True:
    if cells[x][y-1] == 1:
        while (y - 1) > 0:
