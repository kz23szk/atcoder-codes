N = int(input())
left, right = 0, 100000

calc = lambda x: x ** 3 + x

while right - left >= 0.001:
    mid = (left + right) / 2

    if calc(mid) >= N:
        right = mid
    else:
        left = mid

print(right)
