N, S = map(int, input().split())
A = list(map(int, input().split()))

# 1次元配列でもできる
dp = [False for i in range(S+1)]
dp[0] = True

for a in A:
    for i in range(S+1)[::-1]:
        if i - a >= 0:
            dp[i] = dp[i] or dp[i-a]

print("Yes") if dp[-1] else print("No")