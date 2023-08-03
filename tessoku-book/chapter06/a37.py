N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

sumC = sum(C)
total = [len(C) * a + len(C) * B + sumC for a in A]
print(sum(total))
