import heapq

queue = []
N = int(input())
for _ in range(N):
    row = list(map(int, input().split()))
    if len(row) > 1:
        q, price = row
        heapq.heappush(queue, price)
    else:
        q = row[0]
        if q == 2:
            print(queue[0])
        else:
            heapq.heappop(queue)