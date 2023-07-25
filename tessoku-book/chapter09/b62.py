import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
# 隣接リストを作る
ad_list = [set() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

visited = [False] * (N + 1)
path = []


def dfs(pos, v, ad_l):
    path.append(pos)
    # ゴールに着いたら答えを出力して終了
    if pos == N:
        print(*path)
        exit()
    v[pos] = True

    for nex in ad_l[pos]:
        if not v[nex]:
            dfs(nex, v, ad_l)
    path.pop()


dfs(1, visited, ad_list)
