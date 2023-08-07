N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
left = A[0]
right = A[0] * K

while left != right:
    mid = (left + right) // 2
    count = sum([mid // a for a in A])
    if count >= K:
        right = mid
    else:
        left = mid + 1

print(left)
