import heapq

N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    ad_list[a].add((b, c))
    ad_list[b].add((a, c))

MAX = 10 ** 10
cur = [MAX for _ in range(N + 1)]
fixed = [False for _ in range(N + 1)]
cur[1] = 0

queue = []
heapq.heappush(queue, (0, 1))
# キューが空になるまで探索
while queue:
    dist, pos = heapq.heappop(queue)
    if fixed[pos]:
        continue
    fixed[pos] = True
    for nex, dist in ad_list[pos]:
        if cur[nex] > cur[pos] + dist:
            cur[nex] = cur[pos] + dist
            heapq.heappush(queue, (cur[nex], nex))

path = [N]
index = N
while index > 1:
    for pre, dist in ad_list[index]:
        if cur[pre] + dist == cur[index]:
            path.append(pre)
            index = pre
path.reverse()
print(*path)
