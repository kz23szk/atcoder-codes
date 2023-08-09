import sys

N = int(input())
S = list(input())
for i in range(2, N):
    if S[i-2] == S[i-1] == S[i]:
        print("Yes")
        sys.exit(0)
print("No")