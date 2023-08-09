N, M = map(int, input().split())
s = set(range(1, N + 1))
for _ in range(M):
    win, lose = map(int, input().split())
    s.discard(lose)
print(-1 if len(s) != 1 else s.pop())
