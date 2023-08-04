N, K = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(N)]

team_num_list = []
for a in range(1,101):
    for b in range(1, 101):
        team_num = len([1 for i in range(N) if a <= students[i][0] <= a + K and b <= students[i][1] <= b + K])
        team_num_list.append(team_num)

print(max(team_num_list))

