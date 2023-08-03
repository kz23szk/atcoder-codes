N = int(input())
def is_prime(n):
    s = int(n ** 0.5)
    for i in range(2,s+1):
        if n % i == 0:
            return False
    return True

prime_nums = []
for i in range(2, N+1):
    if is_prime(i):
        prime_nums.append(i)
print(*prime_nums)