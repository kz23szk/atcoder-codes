N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False for i in range(S+1)]
dp[0] = True
for a in A:
    for i in range(S+1)[::-1]:
        if i - a >= 0:
            dp[i] = dp[i] or dp[i-a]

print(*dp)

if not dp[-1]:
    print(-1)
else:
    comb = []
    card_i = N - 1
    dp_i = S
    while card_i > 0 or dp_i >0:
        if dp[dp_i - A[card_i]]:
            comb.append(card_i+1)
            dp_i -= A[card_i]
        card_i -= 1

    comb.reverse()
    print(len(comb))
    print(*comb)