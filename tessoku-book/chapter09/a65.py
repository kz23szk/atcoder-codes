N = int(input())
A = list(map(int, input().split()))
buka = [set() for i in range(N+1)]
for i, a in enumerate(A):
    buka[a].add(i+2)

dp = [0 for _ in range(N+1)]
for i in range(1, N+1)[::-1]:
    for b in buka[i]:
        # その部下の部下の数と部下自身を加算する
        dp[i] += dp[b] + 1

print(*dp[1:])

