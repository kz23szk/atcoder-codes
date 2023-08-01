# しゃくとり法で実装
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
r = 1
for i in range(N - 1):
    while r < N and A[r] - A[i] <= K:
        r += 1
    count += r - i - 1
print(count)
