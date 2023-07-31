import sys
N, Y =map(int, input().split())
Y /= 1000
for i in range(2001):
    for j in range(2001-i):
        if N >= i + j and i * 10 + j *5 +(N-i-j) == Y:
            print(i, j, N - i-j)
            sys.exit(0)

print(-1, -1, -1)

