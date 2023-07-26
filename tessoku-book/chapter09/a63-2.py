from collections import deque

n, m = map(int, input().split())
# 隣接リストを作成
ad_list = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

distance = [-1 for _ in range(n + 1)]

queue = deque()
queue.append(1)
distance[1] = 0

while len(queue) > 0:
    pos = queue.popleft()
    for nex in ad_list[pos]:
        if distance[nex] == -1:
            distance[nex] = distance[pos] + 1
            queue.append(nex)

print(*distance[1:], sep="\n")
