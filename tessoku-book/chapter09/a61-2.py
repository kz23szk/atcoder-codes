n, m = map(int, input().split())
ad_list = [set() for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

for i in range(1, n + 1):
    if len(ad_list[i]) == 0:
        print(f"{i}: {{}}")
    else:
        print(f"{i}: {ad_list[i]}")
