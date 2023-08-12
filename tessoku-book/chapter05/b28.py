N = int(input())

div = 10 ** 9 + 7
a = [0] * (N + 1)
a[1] = 1
a[2] = 1
for i in range(3, N + 1):
    a[i] = (a[i - 1] + a[i - 2]) % div

print(a[N])
