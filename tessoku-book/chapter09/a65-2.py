N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]
# i番目の人の部下を格納する配列
buka = [set() for _ in range(N + 1)]
for i, a in enumerate(A):
    buka[a].add(i + 2)

for i in range(1, N + 1)[::-1]:
    for b in buka[i]:
        dp[i] += 1 + dp[b]

print(*dp[1:])
