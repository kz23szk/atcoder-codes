n, r = map(int, input().split())
mod = 1000000007
def factorial_mod(n, m):
    result = 1
    for i in range(2,n+1):
        result = (result * i) % m
    return result

def power_mod(a, b, m):
    digits = []
    while b > 0:
        digits.append(b % 2)
        b //= 2
    p = a
    answer = 1
    for d in digits:
        if d == 1:
            answer = (answer * p) % m
        p = (p * p) % m
    return answer


top = factorial_mod(n, mod)
bottom = factorial_mod(r, mod) * factorial_mod((n-r), mod) % mod

# a / b のmで割ったあまりはmが素数でbがmで割り切れないとき、a / bはa * b ** (m-2)としてよい
print((top * power_mod(bottom, (mod - 2), mod)) % mod)
