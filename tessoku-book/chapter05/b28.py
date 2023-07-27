N = int(input())

a = [1 for _ in range(N + 1)]

MOD = 10 ** 9 + 7
for i in range(3, N + 1):
    a[i] = (a[i - 1] + a[i - 2]) % MOD

print(a[N])
