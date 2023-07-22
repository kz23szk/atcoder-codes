N = int(input())

Left = 0.0
Right = N


def calc(x):
    return x ** 3 + x


while calc((Left + Right) / 2) < N - 0.001 or N + 0.001 < calc((Left + Right) / 2):
    Mid = (Left + Right) / 2
    ans = calc(Mid)
    if ans < N:
        Left = Mid
    else:
        Right = Mid

print((Left + Right) / 2)
