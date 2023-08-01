import sys

N, M = map(int, input().split())
P = []
F = []
for _ in range(N):
    rows = list(map(int, input().split()))
    P.append(rows[0])
    F.append(set(rows[2:]))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if P[i] >= P[j] and F[i] <= F[j] and (P[i] > P[j] or len(F[j] - F[i]) >= 1):
            print("Yes")
            sys.exit(0)
print("No")
