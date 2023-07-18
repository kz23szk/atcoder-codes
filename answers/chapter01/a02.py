N, X = map(int, input().split())
A = list(map(int, input().split()))

flag = False
for a in A:
    if a == X:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
