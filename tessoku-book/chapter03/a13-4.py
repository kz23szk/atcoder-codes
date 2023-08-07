N, K = map(int, input().split())
A = list(map(int, input().split()))
R = 1
count = 0
for i in range(N - 1):
    while R < N and A[R] - A[i] <= K:
        R += 1
    count += R - i - 1

print(count)
