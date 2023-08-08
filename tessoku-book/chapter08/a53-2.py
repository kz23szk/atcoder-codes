import heapq

Q = int(input())
queue = []
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        heapq.heappush(queue, int(q[1]))
    elif q[0] == '2':
        print(queue[0])
    elif q[0] == '3':
        heapq.heappop(queue)
