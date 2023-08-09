N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = M * sum(A) + N * M * B + N * sum(C)
print(ans)
