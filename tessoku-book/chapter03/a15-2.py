import bisect

N = int(input())
A = list(map(int, input().split()))

# リストAの重複を除いた昇順リストを生成する
sortUniqA = sorted(list(set(A)))

B = [bisect.bisect_left(sortUniqA, a) + 1 for a in A]
print(*B)
