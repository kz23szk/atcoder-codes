N , M  = map(int, input().split())
ad_list = [set() for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    ad_list[a].add((b, c))
    ad_list[b].add((a, c))


