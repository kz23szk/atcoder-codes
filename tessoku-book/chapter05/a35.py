N = int(input())
A = list(map(int, input().split()))
sente = N % 2 == 0
while len(A) > 1:
    func = max if sente else min
    A = [func(A[i], A[i+1]) for i in range(len(A)-1)]
    sente = not sente
print(A[0])
