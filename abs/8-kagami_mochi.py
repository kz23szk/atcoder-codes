N = int(input())
d = [int(input()) for _ in range(N)]

# 同じ直径のもち（重複）を省いた個数
print(len(set(d)))
