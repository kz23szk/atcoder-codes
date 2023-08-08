from collections import deque

N, M = map(int, input().split())

# ノード1からそれぞれのノードまでの距離を格納するリスト
distance = [-1 for i in range(N + 1)]
distance[1] = 0

# 隣接リストをつくる
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

# 深さ優先探索
queue = deque()
queue.append(1)
while len(queue) > 0:
    pos = queue.popleft()
    for nex in ad_list[pos]:
        if distance[nex] == -1:
            distance[nex] = distance[pos] + 1
            queue.append(nex)

for d in distance[1:]:
    print(d)
