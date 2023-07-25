N, M = map(int, input().split())
rinsetu = [set()] + [set() for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    rinsetu[A].add(B)
    rinsetu[B].add(A)

for i, r in enumerate(rinsetu[1:]):
    r_list = list(r)
    r_list.sort()
    print(str(i + 1) + ": {", ", ".join([str(i) for i in r_list]), "}", sep="")
