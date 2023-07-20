N = int(input())
A = list(map(int, input().split()))
D = int(input())

for _ in range(D):
    L, R = map(int, input().split())
    print(max(A[:L-1] + A[R:]))

