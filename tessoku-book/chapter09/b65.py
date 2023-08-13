import sys

sys.setrecursionlimit(10 ** 6)

N, T = map(int, input().split())
relations = [tuple(map(int, input().split())) for i in range(N - 1)]
ad_list = [set() for i in range(N + 1)]
for a, b in relations:
    ad_list[a].add(b)
    ad_list[b].add(a)

not_fixed = 1000
dp = [not_fixed for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dp[T] = 0


def dfs(p):
    visited[p] = True
    max_dp = 0
    for buka in ad_list[p]:
        if not visited[buka]:
            dfs(buka)
            if max_dp < dp[buka]:
                max_dp = dp[buka]
    dp[p] = max_dp + 1


dfs(T)
print(*[d - 1 for d in dp[1:]])
