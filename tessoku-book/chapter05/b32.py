N, K = map(int, input().split())
a = list(map(int, input().split()))
min_a = min(a)
max_a = max(a)

win, lose = True, False

dp = [lose for _ in range(N + 1)]
for i in range(1, N + 1):
    if i < min_a:
        dp[i] = lose
    # 1手で0個にできれば勝ち
    elif i in a:
        dp[i] = win
    # 取ったあとのdp[i]が負け状態にできれば勝ち
    elif max([i - e >= 0 and dp[i - e] == lose for e in a]) == True:
        dp[i] = win
    else:
        dp[i] = lose

print("First") if dp[-1] else print("Second")
