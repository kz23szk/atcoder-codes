T = int(input())
N = int(input())
c_sum = [0 for _ in range(T + 1)]
for _ in range(N):
    L, R = map(int, input().split())
    c_sum[L] += 1
    c_sum[R] -= 1

for i in range(1, T + 1):
    c_sum[i] += c_sum[i - 1]

for i in range(T):
    print(c_sum[i])
