N = int(input())

digit = []
for i in range(9, -1, -1):
    digit.append(str((N // 2 ** i) % 2))

print("".join(digit))
