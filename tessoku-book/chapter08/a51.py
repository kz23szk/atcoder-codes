import collections
N = int(input())

queue = collections.deque()
for _ in range(N):
    a= input().split()
    if len(a) > 1:
        q, title = a
        queue.append(title)
    else:
        q = int(a[0])
        if q == 2:
            print(queue[-1])
        else:
            queue.pop()
