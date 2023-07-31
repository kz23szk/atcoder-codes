N, A, B = map(int, input().split())
total = 0


def calc_digits(n):
    digits = 0
    for i in range(5):
        digits += n % 10
        n //= 10
    return digits


for i in range(1, N + 1):
    if A <= calc_digits(i) <= B:
        total += i

print(total)
