N = int(input())
P, A = [0] * N, [0] * N
for i in range(N):
    P[i], A[i] = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
indexes = [i for i in range(N)]
for left in range(N + 1):
    for right in range(N + 1):
        if left + right <= N:
            # 前の状態から右左から取ったときの得点と前の状態の得点の合計の大きい方を算出する
            left_take_point = 0
            right_take_point = 0
            if left > 0:
                left_take_point = dp[left - 1][right]
                if left + 1 <= P[left - 1] < N - right + 1:
                    left_take_point += A[left - 1]
            if right > 0:
                right_take_point = dp[left][right - 1]
                if left + 1 <= P[N - right] < N - right + 1:
                    right_take_point += A[N - right]
            dp[left][right] = max(left_take_point, right_take_point)

last_points = [dp[i][N - i] for i in range(N + 1)]
print(max(last_points))
