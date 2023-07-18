N, Q = map(int, input().split())
A = list(map(int, input().split()))
total = 0
Atotal = [0]
for a in A:
    total += a
    Atotal.append(total)

for i in range(Q):
    L, R = map(int, input().split())
    print(Atotal[R] - Atotal[L - 1])
