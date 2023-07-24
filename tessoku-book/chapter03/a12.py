N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# 二分探索
# Leftは探索範囲の左端を、Rightは右端を表す
Right = K * A[0]  # 一番速度の早いプリンタ1台で印刷したときの秒数がmaxとする
Left = A[0]

while Left < Right:
    Mid = (Right + Left) // 2
    # Mid秒までで合計何枚刷れるか
    print_count = sum([Mid // sec for sec in A])
    if print_count >= K:
        Right = Mid
    else:
        Left = Mid + 1

# 出力このときLeft=Rightになっている
print(Left)
