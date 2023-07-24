# setで解いてみる
N = int(input())
S = list(input())

s = set()
for i, ch in enumerate(S):
    s.add(ch)
    if len(s) == 3:
        print(i + 1)
        break
