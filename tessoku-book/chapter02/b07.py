import itertools

T = int(input())  # 閉店時間
N = int(input())  # 従業員数

zougen = [0] * (T + 1)  # 人の入りと出

for i in range(N):
    L, R = map(int, input().split())
    zougen[L] += 1
    zougen[R] -= 1

# i時にいる人数
ruiseki = list(itertools.accumulate(zougen))

for cnt in ruiseki[:-1]:
    print(cnt)
