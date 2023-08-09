D, N = map(int,input().split())
hours = [24 for _ in range(D+1)]
for _ in range(N):
    L, R, H = map(int, input().split())
    for i in range(L, R+1):
        hours[i] = min(hours[i], H)

print(sum(hours[1:]))