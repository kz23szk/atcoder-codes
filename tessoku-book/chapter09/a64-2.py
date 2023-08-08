import heapq

N, M = map(int, input().split())
# 隣接リストをつくる
ad_list = [set() for i in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    ad_list[A].add((B, C))
    ad_list[B].add((A, C))

INF = 10 ** 10
# 現状での1からの距離をセットするリスト
cur = [INF for i in range(N + 1)]
cur[1] = 0

kakutei = [False for i in range(N + 1)]

priority_queue = []
heapq.heappush(priority_queue, (0, 1))
while len(priority_queue) > 0:
    # 最小となるノードを取り出す
    dist, pos = heapq.heappop(priority_queue)
    if kakutei[pos] == True:
        continue

    kakutei[pos] = True
    # 隣接ノードの距離を計算し、更新できたらキューに詰めて探索対象とする
    for nex, dist in ad_list[pos]:
        prev_cur = cur[nex]
        cur[nex] = min(cur[nex], cur[pos] + dist)
        if cur[nex] < prev_cur:
            heapq.heappush(priority_queue, (cur[nex], nex))

for i in range(1, N + 1):
    if cur[i] == INF:
        print(-1)
    else:
        print(cur[i])
