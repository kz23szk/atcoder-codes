A, B = map(int, input().split())
# 最小公約数をみつける
a, b = A, B
while a % b != 0:
    a, b = b, a % b
gcm = b

print((A // gcm) * (B // gcm) * gcm)
