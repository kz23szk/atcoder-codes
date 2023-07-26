import itertools

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

c_sum = list(itertools.accumulate(a))

for _ in range(q):
    l, r = map(int, input().split())
    print(c_sum[r] - c_sum[l - 1])
