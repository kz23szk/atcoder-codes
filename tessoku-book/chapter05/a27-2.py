A, B = map(int, input().split())
while A % B > 0:
    A, B = B, A % B
print(B)
