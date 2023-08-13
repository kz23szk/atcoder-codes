from collections import deque

N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

queue = deque()
dist = [-1 for i in range(N + 1)]
dist[1] = 0
queue.append(1)
while len(queue) > 0:
    pos = queue.popleft()
    for nex in ad_list[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            queue.append(nex)

print(*dist[1:], sep="\n")
