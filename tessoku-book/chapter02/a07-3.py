from itertools import accumulate

D = int(input())
N = int(input())
attendance_list = [0 for _ in range(D + 2)]
for _ in range(N):
    L, R = map(int, input().split())
    attendance_list[L] += 1
    attendance_list[R + 1] -= 1

c_sum = list(accumulate(attendance_list))
for i in range(1, D + 1):
    print(c_sum[i])
