N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

par, siz = [-1 for _ in range(N + 1)], [1 for _ in range(N + 1)]


# xの根を返す
def root(x):
    while par[x] != -1:
        x = par[x]
    return x


def same(u, v):
    return root(u) == root(v)


def unite(u, v):
    root_u, root_v = root(u), root(v)
    if root_u == root_v:
        return
    if siz[root_u] > siz[root_v]:
        par[root_v] = root_u
        siz[root_u] += siz[root_v]
    else:
        par[root_u] = root_v
        siz[root_v] += siz[root_u]


for q, u, v in queries:
    if q == 1:
        unite(u, v)
    elif q == 2:
        print("Yes") if same(u, v) else print("No")
