N = int(input())
start, end =0, 100000
mid = (start + end) / 2
while abs(N - (mid ** 3 + mid)) > 0.001:
    mid = (start + end) / 2
    ans = mid ** 3 + mid
    if ans >= N:
        end = mid
    else:
        start = mid
print(start)