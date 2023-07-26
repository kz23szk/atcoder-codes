import sys

sys.setrecursionlimit(10 ** 6)
A, B = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(A * B // gcd(A, B))
