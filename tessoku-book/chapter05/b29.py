a, b = map(int, input().split())

binary_digits = []
while b > 0:
    binary_digits.append(b % 2)
    b //= 2

MOD = 10 ** 9 + 7
ans = 1
p = a
for i, digit in enumerate(binary_digits):
    if digit == 1:
        ans = ans * p % MOD
    p = p * p % MOD

print(ans)
