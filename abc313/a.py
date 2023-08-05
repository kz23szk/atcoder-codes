N = int(input())
P = list(map(int, input().split()))
need_x = 0
for i in range(1, N):
    diff = P[i] - P[0]
    if diff >= need_x:
        need_x = diff + 1

print(need_x)