# しゃくとり法でやってみる
N, K = map(int, input().split())
A = list(map(int, input().split()))

i1 = 1
lg_count = [0 for _ in range(N)]
for i in range(N):
    while i1 < N and A[i1] - A[i] <= K:
        i1 += 1
    else:
        lg_count[i] = i1 - i - 1

print(sum(lg_count))
