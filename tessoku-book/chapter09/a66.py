N, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

par = [-1 for _ in range(N + 1)]
siz = [1 for _ in range(N + 1)]


# 根を返す
def root(x):
    while par[x] != -1:
        x = par[x]
    return x


def unite(u, v):
    root_u, root_v = root(u), root(v)
    # 同一グループのときは処理しない
    if root_u == root_v:
        return
    if siz[root_u] < siz[root_v]:
        par[root_u] = root_v
        siz[root_v] += siz[root_u]
    else:
        par[root_v] = root_u
        siz[root_u] += siz[root_v]


def same(u, v):
    return root(u) == root(v)


for q, u, v in queries:
    if q == 1:
        unite(u, v)
    elif q == 2:
        print("Yes") if same(u, v) else print("No")
