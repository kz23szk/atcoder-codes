N = int(input())

prime_factor = []
for i in range(2, int(N**0.5)+1):
    while N % i == 0:
        prime_factor.append(i)
        N //= i
if N >= 2:
    prime_factor.append(N)
print(*prime_factor)
