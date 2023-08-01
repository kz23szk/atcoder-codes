import sys
from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))


def get_all_combination_sum(arr):
    l = [0]
    for n in range(1, len(arr) + 1):
        for c in combinations(arr, n):
            l.append(sum(c))
    return l


A1 = A[:len(A) // 2]
A2 = A[len(A) // 2:]
# リストのままだとTLEだけど、setにすると通る
# 参考：https://qiita.com/kitadakyou/items/6f877edd263f097e78f4
csum_a1, csum_a2 = set(get_all_combination_sum(A1)), set(get_all_combination_sum(A2))
for s in csum_a1:
    if K - s in csum_a2:
        print("Yes")
        sys.exit(0)
print("No")
