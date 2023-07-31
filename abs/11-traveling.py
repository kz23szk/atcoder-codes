import sys

N = int(input())
now_t, now_x, now_y = 0, 0, 0
for _ in range(N):
    t, x, y = map(int, input().split())
    man_kyori = abs(x - now_x) + abs(y - now_y)
    if man_kyori <= t - now_t:
        # 最短で行った場合の余る時間
        spare_time = (t - now_t) - man_kyori
        # とどまれないので上下、左右などで2単位でキリがよければ問題ない
        if spare_time % 2 != 0:
            print("No")
            sys.exit(0)
    else:
        print("No")
        sys.exit(0)
    now_t, now_x, now_y = t, x, y
print("Yes")
