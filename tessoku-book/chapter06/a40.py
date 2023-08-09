N = int(input())
A = list(map(int,input().split()))

d = dict()
# 同じ長さの棒の数を数える
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

def factorial(n):
    val = 1
    for i in range(2, n+1):
        val *= i
    return val

total = 0
# 同じ長さが3本以上あればその組み合わせ数を加算していく
for count in d.values():
    if count >=3:
        total += int(factorial(count) / (factorial(3) * factorial(count - 3)))

print(total)