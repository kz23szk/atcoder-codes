import heapq

N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    ad_list[a].add((b, c))
    ad_list[b].add((a, c))

MAX_DIST = 10 ** 9 + 1
fixed = [False for _ in range(N + 1)]
cur = [MAX_DIST for _ in range(N + 1)]

cur[1] = 0
queue = []
heapq.heappush(queue, (0, 1))
while len(queue) > 0:
    dist, pos = heapq.heappop(queue)
    if fixed[pos]:
        continue
    fixed[pos] = True
    for nex, dist in ad_list[pos]:
        if cur[nex] > cur[pos] + dist:
            cur[nex] = cur[pos] + dist
            heapq.heappush(queue, (cur[nex], nex))

for dist in cur[1:]:
    if dist == MAX_DIST:
        print(-1)
    else:
        print(dist)
