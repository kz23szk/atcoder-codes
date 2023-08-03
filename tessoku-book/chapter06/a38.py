D, N = map(int, input().split())
workHours = [0] + [24 for i in range(D)]
# 条件に沿って労働時間を減らす
for _ in range(N):
    L, R, H = map(int, input().split())
    for d in range(L, R + 1):
        if workHours[d] > H:
            workHours[d] = H
print(sum(workHours))
