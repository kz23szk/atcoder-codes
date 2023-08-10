import sys

A, B = map(int, input().split())
# 100の約数
divisor100 = [i for i in range(1, 101) if 100 % i == 0]

for d in divisor100:
    if A <= d <= B:
        print("Yes")
        sys.exit(0)
print("No")
