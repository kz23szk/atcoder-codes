import sys

N = int(input())
X, Y, Z = [0 for i in range(N)], [0 for i in range(N)], [0 for i in range(N)]
for i in range(N):
    X[i], Y[i], Z[i] = map(int, input().split())

total_giseki = sum(Z)
kahansu =total_giseki // 2 + 1

t_giseki = sum([Z[i] for i in range(N) if X[i] > Y[i]])


if t_giseki >= kahansu:
    print(0)
    sys.exit(0)
# くらがえるかもしれない選曲区番号
kura_kamo_index = [i for i in range(N) if X[i] < Y[i]]

# INF = 10 ** 9
# dp = [[INF for _ in range(total_giseki+1)]for _ in range(len(kura_kamo_index)+1)]
# # 鞍替え0人のとき
# dp[0][t_giseki] = 0
#
# for i, ku in enumerate(kura_kamo_index):
#     for j in range(total_giseki+1):
#         if j-Z[ku] >= 0:
#             dp[i+1][j] = min(dp[i][j], dp[i][j-Z[ku]] + (Y[ku] - X[ku]) // 2 + 1)
#         else:
#             dp[i+1][j] = min(dp[i][j], dp[i+1][j])

INF = 10 ** 9
dp = [[INF for _ in range(kahansu+1)]for _ in range(len(kura_kamo_index)+1)]
# 鞍替え0人のとき
dp[t_giseki][0] = 0

for i, ku in enumerate(kura_kamo_index):
    for j in range(t_giseki, kahansu+1):
        if dp[i][j] != INF:
            # 鞍替えなし
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            # 鞍替え
            saki_j = j + Z[ku] if j + Z[ku] <= kahansu else kahansu
            print(saki_j)
            print((dp[i][saki_j], dp[i][saki_j - Z[ku]] + (Y[ku] - X[ku]) // 2 + 1))
            dp[i + 1][saki_j] = min(dp[i][saki_j], dp[i][saki_j - Z[ku]] + (Y[ku] - X[ku]) // 2 + 1)
    # for j in range(total_giseki + 1):
    #     if j-Z[ku] >= 0:
    #         dp[i+1][j] = min(dp[i][j], dp[i][j-Z[ku]] + (Y[ku] - X[ku]) // 2 + 1)
    #     else:
    #         dp[i+1][j] = min(dp[i][j], dp[i+1][j])

print(dp[-1])
print(dp[-1][-1])


