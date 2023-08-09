N, K = map(int, input().split())
min_step = 2 * (N - 1)
print("Yes") if min_step <= K and (K - min_step) % 2 == 0 else print("No")
