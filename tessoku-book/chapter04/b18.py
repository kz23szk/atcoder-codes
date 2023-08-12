import sys

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if j - A[i] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i]]

if dp[-1][-1] == False:
    print("-1")
    sys.exit(0)

# 復元
cards = []
i = N
j = S
while i > 0:
    # i番目を選んだ
    if dp[i - 1][j] == False:
        j -= A[i]
        cards.append(i)
    i -= 1

cards.reverse()
print(len(cards))
print(*cards)
