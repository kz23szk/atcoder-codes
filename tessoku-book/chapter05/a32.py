N, A, B = map(int, input().split())
# 残りがi個で先手の手番のとき勝ちならTrue、負けならFalseを格納するdp
dp = [False for _ in range(N + 1)]
for i in range(A, N + 1):
    # 最終盤で一手でのこりの石がA個未満になれば勝ち
    if 0 <= i - A < A or 0 <= i - B < A:
        dp[i] = True
    # AかBを取った先がFalse、つまり相手が負けの盤面になれば勝ち
    elif not dp[i - A] or not dp[i - B]:
        dp[i] = True

print("First") if dp[-1] else print("Second")
