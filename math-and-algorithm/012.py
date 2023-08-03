N = int(input())


def is_prime(n):
    s = int(n ** 0.5)
    for i in range(2, s + 1):
        if n % i == 0:
            return False
    return True


if is_prime(N):
    print("Yes")
else:
    print("No")
