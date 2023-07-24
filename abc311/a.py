N = int(input())
S = list(input())
A, B, C = False, False, False
for i, s in enumerate(S):
    if s == 'A':
        A = True
    elif s == 'B':
        B = True
    else:
        C = True
    if A and B and C:
        print(i + 1)
        break
