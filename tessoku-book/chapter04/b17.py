N = int(input())
H = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]
dp[2] = abs(H[1] - H[2])
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

path = [N]
i = N
# 経路の復元
while i > 1:
    if dp[i] - dp[i - 2] == abs(H[i - 2] - H[i]):
        i -= 2
    else:
        i -= 1
    path.append(i)
path.reverse()

print(len(path))
print(*path)
