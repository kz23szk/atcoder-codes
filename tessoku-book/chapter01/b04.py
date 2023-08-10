N = list(map(int, list(input())))
num = 0

for i, digit in enumerate(N[::-1]):
    if digit == 1:
        num += 2 ** i

print(num)
