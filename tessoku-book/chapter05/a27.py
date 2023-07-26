import sys

sys.setrecursionlimit(10 ** 6)


def gcd(a, b):
    small, big = min(a, b), max(a, b)
    if small == 0:
        return big
    return gcd(big % small, small)


a, b = map(int, input().split())
print(gcd(a, b))
