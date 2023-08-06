N, K = map(int, input().split())

combination = [1 for i in range(1, N+1) for j in range(1, N+1) if 1 <= K - i - j <= N]
print(len(combination))
