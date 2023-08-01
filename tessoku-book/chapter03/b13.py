# しゃくとり法で実装
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
c_sum = [0] + list(itertools.accumulate(A))
count = 0
r = 1
for i in range(1, N+1):
    while r <= N and c_sum[r] - c_sum[i-1] <= K:
        r += 1
    count += r - i
print(count)
