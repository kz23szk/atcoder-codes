import sys

sys.setrecursionlimit(10 ** 9)
N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

visited = [False for _ in range(N + 1)]


def dfs(pos):
    visited[pos] = True
    for nex in ad_list[pos]:
        if not visited[nex]:
            dfs(nex)


dfs(1)
if min(visited[1:]) == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
