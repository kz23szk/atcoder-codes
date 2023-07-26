import math

N = int(input())
h = list(map(int, input().split()))
dp = [math.inf for _ in h]
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, len(h)):
    root1 = abs(h[i] - h[i - 1]) + dp[i - 1]
    root2 = abs(h[i] - h[i - 2]) + dp[i - 2]
    dp[i] = min(root1, root2)

# 経路の復元
path = []
index = len(h) - 1
while index >= 1:
    path.append(index + 1)
    if dp[index] == dp[index - 1] + abs(h[index] - h[index - 1]):
        index -= 1
    else:
        index -= 2

path.append(1)
path.sort()
print(len(path))
print(*path)
