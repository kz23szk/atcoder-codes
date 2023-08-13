N = int(input())
C = [0 for i in range(N)]
A = []
for i in range(N):
    C[i] = int(input())
    A.append(list(map(int, input().split())))

X = int(input())
min_bet = 38
for i in range(N):
    if X in A[i] and min_bet > len(A[i]):
        min_bet = len(A[i])

winner = []
for i in range(N):
    if X in A[i] and len(A[i]) == min_bet:
        winner.append(i+1)
print(len(winner))
print(*winner)