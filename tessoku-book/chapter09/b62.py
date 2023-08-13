import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

prev_pos = [-1 for i in range(N + 1)]
visited = [False for _ in range(N + 1)]


def dfs(pos):
    visited[pos] = True
    for nex in ad_list[pos]:
        if not visited[nex]:
            prev_pos[nex] = pos
            dfs(nex)


dfs(1)
pos = N
path = []
while pos != -1:
    path.append(pos)
    pos = prev_pos[pos]

path.reverse()
print(*path)
