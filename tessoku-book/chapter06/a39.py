N = int(input())
movies = [tuple(map(int, input().split())) for _ in range(N)]
# 終わるのが早い順にソートする
movies.sort(key=lambda x: x[1])
current_time = 0
count = 0
for start, end in movies:
    # 始まる前なら鑑賞できて、終了時間まで経過させる
    if current_time <= start:
        count += 1
        current_time = end

print(count)
