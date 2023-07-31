N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    mods = [a % 2 for a in A]
    # すべて割り切れるなら
    if max(mods) == 0:
        A = [a // 2 for a in A]
        count += 1
    else:
        print(count)
        break
