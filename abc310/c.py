N = int(input())
uniq_strs = set()
for _ in range(N):
    s = input()
    if s not in uniq_strs and s[::-1] not in uniq_strs:
        uniq_strs.add(s)
print(len(uniq_strs))
