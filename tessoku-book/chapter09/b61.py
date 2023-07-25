N, M = map(int, input().split())
friendship = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    friendship[a - 1].add(b - 1)
    friendship[b - 1].add(a - 1)

max_index = 0
max_cnt = 0
for i, f in enumerate(friendship):
    cnt = len(f)
    if cnt > max_cnt:
        max_cnt = cnt
        max_index = i

print(max_index + 1)
