N, X, Y = map(int, input().split())
is_X_or_Y_times = [1 for i in range(1, N + 1) if i % X == 0 or i % Y == 0]
print(len(is_X_or_Y_times))
