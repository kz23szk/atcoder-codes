N = int(input())
blocks = [tuple(map(int, input().split())) for i in range(N)]


# 操作したときに得られる点数
def get_point(l_or_r, l, r, bs):
    if l_or_r == 'r':
        p, a = bs[N - r]
    else:
        p, a = bs[l - 1]
    if l + 1 <= p < N - r + 1:
        return a
    return 0


max_point = 0
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 全部左から取った場合のdp
for l in range(1, N + 1):
    dp[l][0] = dp[l - 1][0] + get_point("l", l, 0, blocks)

# 全部右から取った場合のdp
for r in range(1, N + 1):
    dp[0][r] = dp[0][r - 1] + get_point("r", 0, r, blocks)

for l in range(1, N + 1):
    for r in range(1, N + 1):
        if l + r <= N:
            dp[l][r] = max(dp[l - 1][r] + get_point("l", l, r, blocks), dp[l][r - 1] + get_point("r", l, r, blocks))
        if l + r == N:
            if dp[l][r] > max_point:
                max_point = dp[l][r]

# 操作が終わったとき(操作回数の合計がN)の得点を抽出
end_operations = [dp[i][N - i] for i in range(N + 1)]
print(max(end_operations))
