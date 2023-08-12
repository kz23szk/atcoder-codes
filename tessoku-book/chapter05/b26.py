# エラトステネスのふるい
N = int(input())
candidates = [True for i in range(N + 1)]
candidates[0] = False
candidates[1] = False


def is_prime_number(n):
    max_candidate = int(n ** 0.5)
    for i in range(2, max_candidate + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, N + 1):
    if candidates[i]:
        num = i + i
        while num <= N:
            candidates[num] = False
            num += i

prime_nums = [i for i, prime in enumerate(candidates) if prime]
print(*prime_nums, sep='\n')
