import heapq

N, M = map(int, input().split())
ad_list = [set() for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    ad_list[a].add((b, c))
    ad_list[b].add((a, c))

max_dist = 10 ** 10
cur = [max_dist for i in range(N + 1)]
cur[1] = 0
priority_queue = []
heapq.heappush(priority_queue, (0, 1))
kakutei = [ False for _ in range(N+1)]

while len(priority_queue) > 0:
    _, pos = heapq.heappop(priority_queue)

    if kakutei[pos] == True:
        continue

    kakutei[pos] = True
    for nex, dist in ad_list[pos]:
        prev_cur = cur[nex]
        cur[nex] = min(cur[nex], cur[pos] + dist)
        if cur[nex] < prev_cur:
            heapq.heappush(priority_queue, (cur[nex], nex))

for i in range(1, N + 1):
    if cur[i] == max_dist:
        print(-1)
    else:
        print(cur[i])
