N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

path = [N]
i = N
while i > 1:
    if dp[i] - dp[i - 1] == A[i]:
        i -= 1
    else:
        i -= 2
    path.append(i)
path.reverse()
print(len(path))
print(*path)
