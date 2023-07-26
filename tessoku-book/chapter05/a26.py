Q = int(input())
for _ in range(Q):
    X = int(input())
    limit = int(X ** 0.5)  # 素数でない場合は√n以下の約数を持つのでここまでチェックする
    is_prime = True
    for i in range(2, limit + 1):
        if X % i == 0:
            is_prime = False
    print("Yes") if is_prime else print("No")
