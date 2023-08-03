from itertools import accumulate
import operator

A = list(map(int, input().split()))
cum_p = list(accumulate(A, func=operator.mul))
print(cum_p[-1])
