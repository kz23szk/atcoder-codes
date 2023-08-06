N = int(input())
A = [0] + list(map(int, input().split()))
# 1部屋目からその部屋までの最大人数を格納する
max_A_from_left = [0] * (N + 1)
for i in range(1, N + 1):
    max_A_from_left[i] = max(A[i], max_A_from_left[i - 1])

# N部屋目からその部屋までの最大人数を格納する
max_A_from_right = [0] * (N + 2)
for i in range(1, N + 1)[::-1]:
    max_A_from_right[i] = max(A[i], max_A_from_right[i + 1])

D = int(input())
for _ in range(D):
    L, R = map(int, input().split())
    print(max(max_A_from_left[L - 1], max_A_from_right[R + 1]))
