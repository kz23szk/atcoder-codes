N = int(input())

num = []
while N > 0:
    num.append(N % 2)
    N //= 2

num.reverse()
num = list(map(str, num))
num_str = "".join(num)

print(num_str.zfill(10))
