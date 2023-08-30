N = int(input())
h = [0] + list(map(int, input().split()))

INF = 10 ** 10
dp = [INF for i in range(N+1)]
dp[0] = 0
dp[1] = 0
dp[2] = abs(h[2] - h[1])

for i in range(3, N):
    step1 = abs(h[i] - h[i-1])
    step2 = abs(h[i] - h[i - 2])
    dp[i] = min(step1 + dp[i-1], step2 + dp[i-2])

path = [N]
i = N
while i > 1:
    if dp[i] - dp[i-1] == abs(h[i] - h[i-1]):
        i -= 1
    else:
        i -= 2
    path.append(i)

path.reverse()
print(len(path))
print(*path)