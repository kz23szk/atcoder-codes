import itertools

D = int(input())
N = int(input())

zougen = [0 for i in range(D + 2)]
for _ in range(N):
    L, R = map(int, input().split())
    zougen[L] += 1
    zougen[R + 1] -= 1

attendance_cnt = list(itertools.accumulate(zougen))

for cnt in attendance_cnt[1:-1]:
    print(cnt)
