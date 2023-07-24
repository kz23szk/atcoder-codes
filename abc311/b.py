N, D = map(int, input().split())
all_attendance = [True for i in range(D)]
for _ in range(N):
    S = [True if i == 'o' else False for i in list(input())]
    for i, b in enumerate(S):
        if not b:
            all_attendance[i] = False

max_count = 0
for i, b in enumerate(all_attendance):
    if b:
        count = 1
        for j in range(i + 1, len(all_attendance)):
            if all_attendance[j]:
                count += 1
            else:
                if max_count <= count:
                    max_count = count
                break

            if j == len(all_attendance) - 1:
                if max_count <= count:
                    max_count = count
        # xxxxxxoの救済
        if max_count == 0 and i == len(all_attendance) - 1:
            max_count = 1
print(max_count)
