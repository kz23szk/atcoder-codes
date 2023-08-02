N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
max_val = 100000 * 100 + 1
dp = [max_val for _ in range(N)]
dp[0], dp[1] = 0, A[1]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

index = N - 1
path = [N]
while index > 0:
    if dp[index] - dp[index - 2] == B[index]:
        index -= 2
    else:
        index -= 1
    path.append(index + 1)
path.reverse()
print(len(path))
print(*path)
