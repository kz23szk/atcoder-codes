D = int(input())
N = int(input())

ruiseki = [0 for i in range(D+1)]
for i in range(N):
    L, R = map(int, input().split())
    for j in range(L, R+1):
        ruiseki[j] += 1

for i in range(1, D+1):
    print(ruiseki[i])

