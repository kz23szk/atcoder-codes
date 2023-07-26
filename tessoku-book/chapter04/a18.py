import itertools

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False for _ in range(S + 1)] for _ in range(len(A) + 1)]

dp[0][0] = True

for i in range(1, len(A) + 1):
    for j in range(S + 1):
        if dp[i - 1][j]:
            # 選ぶ
            if j + A[i - 1] <= S:
                dp[i][j + A[i - 1]] = True
            # 選ばない
            dp[i][j] = True

last_list = [row[-1] for row in dp]
print("Yes") if max(last_list) else print("No")
