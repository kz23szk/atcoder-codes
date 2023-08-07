Q = int(input())


def is_prime(n):
    check_max_num = int(n ** 0.5)
    for i in range(2, check_max_num + 1):
        if n % i == 0:
            return False
    return True


for _ in range(Q):
    n = int(input())
    print("Yes") if is_prime(n) else print("No")
