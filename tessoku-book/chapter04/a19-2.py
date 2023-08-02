N, W = map(int, input().split())
w, v = [0], [0]
for _ in range(N):
    w1, v1 = map(int, input().split())
    w.append(w1)
    v.append(v1)

dp = [[0 for i in range(W+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(W+1):
        if j - w[i] < 0:
            dp[i][j]= dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

max_v = 0
for row in dp:
    if max(row) > max_v:
        max_v = max(row)
print(max_v)
