N = int(input())
blocks = [tuple(map(int, input().split())) for i in range(N)]

indexs = [i+1 for i in range(N)]
def get_point(l_or_r, l, r, bs):
    print(l, r, indexs[l:N-r])
    if l_or_r == 'r':
        p, a = bs[N-r]
    else:
        p, a = bs[l-1]
    if l+1 <= p < N -r + 1: #  in indexs[l:N-r]:
        return a
    return 0

max_point = 0
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for l in range(N+1):
    for r in range(N+1):
        if l + r <= N:
            if r == 0 and l == 0:
                dp[l][r] = 0
            elif r == 0:
                dp[l][r] = dp[l-1][r] + get_point("l", l, r, blocks)
            elif l == 0:
                dp[l][r] = dp[l][r-1] + get_point("r", l, r, blocks)
            else:
                dp[l][r] = max(dp[l-1][r] + get_point("l", l, r, blocks), dp[l][r-1] + get_point("r", l, r, blocks))
        if l + r == N:
            if dp[l][r] > max_point:
                max_point = dp[l][r]

for row in dp:
    print(*row)
print(max_point)
