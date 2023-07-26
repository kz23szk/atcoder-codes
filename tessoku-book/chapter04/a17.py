import math

N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

min_times = [math.inf for i in range(N + 1)]
prev_path = [-1 for i in range(N + 1)]
min_times[1] = 0
min_times[2] = A[2]
prev_path[1] = 0
prev_path[2] = 1
for i in range(3, N + 1):
    rootA_time = A[i] + min_times[i - 1]
    rootB_time = B[i] + min_times[i - 2]
    if rootA_time <= rootB_time:
        min_times[i] = rootA_time
        prev_path[i] = i - 1
    else:
        min_times[i] = rootB_time
        prev_path[i] = i - 2

path = []
index = N
while index > 0:
    path.append(index)
    index = prev_path[index]

print(len(path))
path.reverse()
print(*path)
