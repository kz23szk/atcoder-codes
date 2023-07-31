N, K = map(int, input().split())
A = list(map(int, input().split()))
start, end = 1, 10 ** 9
while start != end:
    mid = (start + end) // 2
    count = sum([mid // a for a in A])
    if count >= K:
        end = mid
    else:
        start = mid + 1
print(start)
