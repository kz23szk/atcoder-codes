import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
# 隣接リストを作る
ad_list = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

# 一つ前のノードを記録
prev = [-1 for _ in range(n + 1)]
prev[1] = 1


def dfs(pos, ad_list):
    for nex in ad_list[pos]:
        if prev[nex] == -1:
            prev[nex] = pos
            dfs(nex, ad_list)


dfs(1, ad_list)
index = n
path = [n]
while prev[index] != 1:
    path.append(prev[index])
    index = prev[index]
path.append(1)

path.reverse()
print(*path)
