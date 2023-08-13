N , M =map(int, input().split())
roulettes = [list(map(int, input().split())) for i in range(N)]
C, AVG , cosp = [0] * N, [0] * N, [0] * N

min_cosp = 10000000000
best_index = -1
for i, r in enumerate(roulettes):
    C[i], AVG[i] = r[0], sum(r[2:])/ r[1]
    cosp[i] = AVG[i] / C[i]
    if min_cosp > cosp[i]:
        min_cosp = cosp[i]
        best_index = i

print(M / AVG[best_index] * C[best_index])
