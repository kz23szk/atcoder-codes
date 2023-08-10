N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())


def search(n, l):
    left, right = 0, len(l) - 1

    while right != left:
        mid = (left + right) // 2
        if l[mid] >= n:
            right = mid
        else:
            left = mid + 1
    if l[left] < n:
        return left + 1
    return left


for _ in range(Q):
    x = int(input())
    print(search(x, A))
