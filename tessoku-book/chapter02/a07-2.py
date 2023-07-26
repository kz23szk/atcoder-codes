from itertools import accumulate

d = int(input())
n = int(input())

updown = [0 for _ in range(d + 2)]
for _ in range(n):
    left, right = map(int, input().split())
    updown[left] += 1
    updown[right + 1] -= 1

# 累積和を計算
c_sum = list(accumulate(updown))
print(*c_sum[1:-1], sep='\n')
