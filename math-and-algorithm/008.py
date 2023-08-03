N, S = map(int, input().split())

pattern = [min(S - i, N) for i in range(1, N + 1) if S - i > 0]
print(sum(pattern))
