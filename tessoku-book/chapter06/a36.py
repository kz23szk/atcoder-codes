N, K = map(int, input().split())

need_step = 2 * (N - 1)
if need_step <= K and (K - need_step) % 2 == 0:
    print("Yes")
else:
    print("No")
