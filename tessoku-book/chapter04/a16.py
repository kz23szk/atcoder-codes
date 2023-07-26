import math

N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

min_times = [math.inf for i in range(N + 1)]
min_times[0] = 0
min_times[1] = 0
min_times[2] = A[2]
for i in range(3, N + 1):
    rootA_time = A[i] + min_times[i - 1]
    rootB_time = B[i] + min_times[i - 2]
    min_times[i] = min(rootA_time, rootB_time)

print(min_times[N])
