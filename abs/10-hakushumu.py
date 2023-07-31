S = input()
s1 = 'dream'
s2 = 'dreamer'
s3 = 'erase'
s4 = 'eraser'

while True:
    if S.endswith(s2):
        S = S[:-7]
    elif S.endswith(s4):
        S = S[:-6]
    elif S.endswith(s1) or S.endswith(s3):
        S = S[:-5]
    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")