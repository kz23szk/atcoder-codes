from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    row = input().split()
    if len(row) > 1:
        q, name = row
        queue.append(name)
    else:
        q = int(row[0])
        if q == 2:
            print(queue[0])
        else:
            queue.popleft()