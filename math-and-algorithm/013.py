N = int(input())

divisor = []
rootN = N ** 0.5
for i in range(1, int(rootN) + 1):
    if N % i == 0:
        divisor.append(i)
        divisor.append(N // i)

for d in divisor:
    print(d)
