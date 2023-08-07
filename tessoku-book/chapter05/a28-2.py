N = int(input())
n = 0
for _ in range(N):
    operator, num = input().split()
    num = int(num)
    if operator == '+':
        n += num
    elif operator == '-':
        n -= num
    elif operator == '*':
        n *= num
    n %= 10000
    print(n)

