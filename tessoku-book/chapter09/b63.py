from collections import deque

r, c = map(int, input().split())
start_y, start_x = map(int, input().split())
end_y, end_x = map(int, input().split())
# indexが0始まり都合でそれぞれ-1する
start_y, start_x, end_y, end_x = start_y - 1, start_x - 1, end_y - 1, end_x - 1

# 迷路を格納する二次元配列(Trueは通れる)
cells = [[False for _ in range(c)] for _ in range(r)]
for i in range(r):
    cell = list(input())
    cells[i] = [True if s == "." else False for s in cell]

# スタート地点からの距離を初期化
distance = [[-1 for _ in range(c)] for _ in range(r)]
distance[start_y][start_x] = 0

# 幅優先探索する
queue = deque()
queue.append((start_y, start_x))


# 移動可能な上下左右のセルを返す
def get_movable_cells(y, x, cells):
    m_cells = []
    if cells[y - 1][x]:
        m_cells.append((y - 1, x))
    if cells[y + 1][x]:
        m_cells.append((y + 1, x))
    if cells[y][x - 1]:
        m_cells.append((y, x - 1))
    if cells[y][x + 1]:
        m_cells.append((y, x + 1))
    return m_cells


while len(queue) > 0:
    posy, posx = queue.popleft()
    movable_cells = get_movable_cells(posy, posx, cells)
    for nex in movable_cells:
        y, x = nex
        if distance[y][x] == -1:
            queue.append(nex)
            distance[y][x] = distance[posy][posx] + 1

print(distance[end_y][end_x])
