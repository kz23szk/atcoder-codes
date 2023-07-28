N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False for _ in range(S+1)] for _ in range(len(A)+1)]

dp[0][0] = True
for i in range(1, len(A)+1):
    for j in range(S+1):
        dp[i][j] = dp[i-1][j] or dp[i][j]
        if j + A[i-1] <= S:
            dp[i][j+A[i-1]] = True and dp[i-1][j]

exist = False
cards = []
for i, row in enumerate(dp):
    if row[-1]:
        exist = True
        w_index = S
        h_index = i
        while w_index > 0:
            if not dp[h_index-1][w_index]:
                cards.append(h_index)
                w_index -= A[h_index-1]
            else:
                h_index -= 1
        break

if exist:
    cards.reverse()
    print(len(cards))
    print(*cards)
else:
    print(-1)


