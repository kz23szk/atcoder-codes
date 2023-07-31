N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N - 1
while left != right:
    mid = (left + right) // 2
    if X <= A[mid]:
        right = mid
    else:
        left = mid + 1
print(left + 1)
