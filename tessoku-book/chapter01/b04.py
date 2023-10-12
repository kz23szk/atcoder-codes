N = input()
N = reversed(N)
num = 0
for i, n in enumerate(N):
    if int(n) == 1:
        num += 2 ** i

print(num)
