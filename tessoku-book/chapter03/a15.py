import bisect

N = int(input())
A = list(map(int, input().split()))

# 重複を削除して、小さい順に並べたAのリストを用意する
setA = set(A)
sortA = sorted(list(setA))

B = []
for a in A:
    index = bisect.bisect(sortA, a)
    B.append(index)
print(*B)
