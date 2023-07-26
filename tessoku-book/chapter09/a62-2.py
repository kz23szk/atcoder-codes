import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
# 隣接リストを作成
ad_list = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b, = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

# いったことのある頂点を記録する配列
visited = [False for _ in range(n + 1)]


def dfs(pos, a, visited):
    visited[pos] = True
    for nex in a[pos]:
        if not visited[nex]:
            dfs(nex, a, visited)


dfs(1, ad_list, visited)
# 一箇所でも繋がってなければ連結していない
if min(visited[1:]) == False:
    print("The graph is not connected.")
else:
    print("The graph is connected.")
