N, K = map(int, input().split())
A = list(map(int, input().split()))

i = 0
R = 0
pattern = 0
while i < N:
    while True:
        if sum(A[i: R + 1]) <= K:
            if R == N:
                pattern += R - i
                break
            R += 1
        else:
            pattern += R - i
            break
    i += 1
print(pattern)
