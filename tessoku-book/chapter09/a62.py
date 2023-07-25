import sys

sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
ad_list = [set() for _ in range(N)]
visited = [False for i in range(N)]

# 隣接リストを作る
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a - 1].add(b - 1)
    ad_list[b - 1].add(a - 1)


def dfs(pos):
    visited[pos] = True
    # 隣接点をすべて探索しにいき、いったことがなければ探索する
    for nex in ad_list[pos]:
        if not visited[nex]:
            dfs(nex)


dfs(0)
answer = "The graph is connected." if min(visited) else "The graph is not connected."
print(answer)
