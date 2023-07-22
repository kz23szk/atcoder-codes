N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_sec = K * A[0]  # 一番速度の早いプリンタ1台で印刷したときの秒数がmaxとする
min_sec = A[0]

check_sec = 0
while True:
    check_sec = (max_sec + min_sec) // 2
    # check_secまでで合計何枚刷れるか
    print_count = sum([check_sec // sec for sec in A])
    if print_count == K:
        break
    elif print_count > K:
        print_count_before_1_sec = sum([(check_sec - 1) // sec for sec in A])
        if K > print_count_before_1_sec:
            break
        max_sec = check_sec
    else:
        min_sec = check_sec

print(check_sec)
