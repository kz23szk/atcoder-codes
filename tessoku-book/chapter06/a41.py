import sys

N = int(input())
S = list(input())

for i in range(N - 2):
    if S[i] == S[i + 1] == S[i + 2]:
        print("Yes")
        sys.exit(0)
print("No")
