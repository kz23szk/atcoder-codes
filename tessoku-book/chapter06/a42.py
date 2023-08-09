N, K = map(int, input().split())
A, B = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    A[i], B[i] = map(int, input().split())

max_team_num = 0
for i in range(1, 101):
    for j in range(1, 101):
        # 下限を体力i,気力jとしたときに iからi+K、jからj+Kを満たす人数を数える
        count = len([1 for k in range(N) if i <= A[k] <= i + K and j <= B[k] <= j + K])
        max_team_num = count if max_team_num < count else max_team_num

print(max_team_num)
