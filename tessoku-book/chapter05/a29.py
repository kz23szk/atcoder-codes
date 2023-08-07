a, b = map(int, input().split())
m = 10 ** 9 + 7

# bの2進数を計算する
b_2digit = []
while b > 0:
    b_2digit.append(b % 2)
    b //= 2
# b= 23のとき、[1,1,1,0,1]となり、
# a**1 + a**2 + a**4 + a**16 = a**23 と展開できることが分かる

p = a
answer = 1
for digit in b_2digit:
    if digit == 1:
        # a ** n + a ** i の余りを計算する
        answer = (answer * p) % m
    # a ** iの余りを計算しておく
    p = (p * p) % m
print(answer)
