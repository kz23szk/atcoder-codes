N = int(input())
movies = [ tuple(map(int, input().split())) for _ in range(N)]
# 終了時刻、開始時刻で並び替え
movies.sort(key=lambda x: (x[1], x[0]))

current_time = 0
watch_count = 0
for movie in movies:
    start, end = movie
    if current_time <= start:
        current_time = end
        watch_count += 1

print(watch_count)