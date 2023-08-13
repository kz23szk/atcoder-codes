N, M = map(int, input().split())
ad_list = [set() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    ad_list[a].add(b)
    ad_list[b].add(a)

max_friends = 0
max_index = -1
for i in range(1, N + 1):
    if max_friends < len(ad_list[i]):
        max_friends = len(ad_list[i])
        max_index = i

print(max_index)
