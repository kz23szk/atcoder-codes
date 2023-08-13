from collections import deque

R, C = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
cells = [[]]
for i in range(R):
    cells.append([0] + list(input()))

cost = [[2501 for _ in range(C + 1)] for _ in range(R + 1)]
cost[start_y][start_x] = 0
visited = [[False for _ in range(C + 1)] for _ in range(R + 1)]
queue = deque()
queue.append((start_y, start_x))
while queue:
    y, x = queue.popleft()
    for next_y, next_x in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if cells[next_y][next_x] == '.' and not visited[next_y][next_x]:
            cost[next_y][next_x] = min(cost[next_y][next_x], cost[y][x] + 1)
            queue.append((next_y, next_x))
            visited[next_y][next_x] = True

print(cost[goal_y][goal_x])
