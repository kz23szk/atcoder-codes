N = int(input())
A = [0] + list(map(int, input().split()))
c_sum_win, c_sum_lose = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    c_sum_win[i] += c_sum_win[i - 1]
    c_sum_lose[i] += c_sum_lose[i - 1]
    if A[i] == 1:
        c_sum_win[i] += 1
    else:
        c_sum_lose[i] += 1

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    win_count, lose_count = c_sum_win[R] - c_sum_win[L - 1], c_sum_lose[R] - c_sum_lose[L - 1]
    if win_count > lose_count:
        print("win")
    elif win_count == lose_count:
        print("draw")
    else:
        print("lose")
