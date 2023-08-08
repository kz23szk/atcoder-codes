from collections import deque

Q = int(input())
queue = deque()
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        queue.append(q[1])
    elif q[0] == '2':
        print(queue[-1])
    elif q[0] == '3':
        queue.pop()
