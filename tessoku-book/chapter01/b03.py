import sys
import itertools

N = int(input())
A = list(map(int, input().split()))

for c in itertools.combinations(A, 3):
    if sum(c) == 1000:
        print("Yes")
        sys.exit(0)
print("No")

