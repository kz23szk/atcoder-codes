H, W = map(int, input().split())
mod = 1000000007


def fact(n, m):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
        ans %= m
    return ans


# 移動回数
n = H - 1 + W - 1
# そのうち下方向の移動の回数
r = H - 1

# 組合せの分母と分子を計算
top = fact(n, mod)
bottom = fact(n - r, mod) * fact(r, mod)


# 繰り返し二乗法 pow関数でも同じ
def orig_pow(a, b, m):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans *= a
            ans %= m
        b //= 2
        a *= a
        a %= mod
    return ans


print(top * orig_pow(bottom, mod - 2, mod) % mod)
