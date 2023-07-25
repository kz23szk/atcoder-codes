from collections import deque

N, M = map(int, input().split())

# 隣接リストを作る
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    ad_list[A].add(B)
    ad_list[B].add(A)

dist = [-1 for i in range(N + 1)]
queue = deque()
queue.append(1)
dist[1] = 0
while len(queue) > 0:
    pos = queue.popleft()
    for nex in ad_list[pos]:
        if dist[nex] == -1:
            queue.append(nex)
            dist[nex] = dist[pos] + 1

for d in dist[1:]:
    print(d)

