A, B = map(int, input().split())

flag = False
for n in range(A, B + 1):
    if 100 % n == 0:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
