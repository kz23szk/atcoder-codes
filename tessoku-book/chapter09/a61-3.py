N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

for i in range(1, N + 1):
    if len(ad_list[i]) == 0:
        print(f"{i}: {{}}")
    else:
        print(f"{i}: {ad_list[i]}")
