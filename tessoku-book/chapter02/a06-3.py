from itertools import accumulate

N, Q = map(int, input().split())
A = list(map(int, input().split()))
c_sum = [0] + list(accumulate(A))
for _ in range(Q):
    l, r = map(int, input().split())
    print(c_sum[r] - c_sum[l - 1])
