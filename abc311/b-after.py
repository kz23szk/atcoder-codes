N, D = map(int, input().split())
all_attendance = [True for i in range(D)]
for _ in range(N):
    S = [True if i == 'o' else False for i in list(input())]
    for i, b in enumerate(S):
        if not b:
            all_attendance[i] = False

ruiseki = [0] * len(all_attendance)
for i, shusseki in enumerate(all_attendance):
    if i == 0:
        ruiseki[i] = 1 if shusseki else 0
    elif shusseki:
        ruiseki[i] = ruiseki[i - 1] + 1

print(max(ruiseki))
