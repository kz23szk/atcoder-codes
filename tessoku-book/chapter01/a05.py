N, K = map(int, input().split())

cnt = 0
for red in range(1, N+1):
    for blue in range(1, N+1):
        if N + 1 > K - red - blue > 0:
            cnt += 1

print(cnt)