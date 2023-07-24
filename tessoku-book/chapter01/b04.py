N = [int(c) for c in input()]
N.reverse()

val = 0
for i, n in enumerate(N):
    if n == 1:
        val += 2 ** i

print(val)
