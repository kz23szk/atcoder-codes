N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())


def search(x, l):
    start = 0
    end = N
    while end != start:
        mid = (start + end) // 2
        if x <= l[mid]:
            end = mid
        else:
            start = mid + 1
    return start


for _ in range(Q):
    print(search(int(input()), A))
