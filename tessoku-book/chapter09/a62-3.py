import sys

sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
ad_list = [set() for _ in range(N + 1)]
for a, b in edges:
    ad_list[a].add(b)
    ad_list[b].add(a)

visited = [False for _ in range(N + 1)]


def dfs(pos):
    visited[pos] = True
    nex = ad_list[pos]
    for n in nex:
        if not visited[n]:
            dfs(n)


# 1からたどる
dfs(1)
# 1 ~ N が全てTrueなら連結している
if min(visited[1:]) == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
