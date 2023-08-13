N = int(input())
S = list(input())
Q = int(input())

upper = 0 # 操作なし 0 upper 1 lower 2
operator = []
for i in range(Q):
    operator.append(tuple(input().split()))

last_upper_or_lower_index = -1
upper = False
for i in range(Q)[::-1]:
    t=  int(operator[i][0])
    if t != 1:
        last_upper_or_lower_index = i
        upper = t == 3
        break
# 大文字小文字操作がないとき
if last_upper_or_lower_index == -1:
    for i in range(Q):
        t, x, c = operator[i]
        if t == '1':
            S[int(x)-1] = c
else:
    for i in range(last_upper_or_lower_index+1):
        t, x, c = operator[i]
        if t == '1':
            S[int(x)-1] = c
    S = "".join(S)
    if upper:
        S = S.upper()
    else:
        S = S.lower()
    S = list(S)
    for i in range(last_upper_or_lower_index+1, Q):
        t, x, c = operator[i]
        if t == '1':
            S[int(x)-1] = c

print("".join(S))
