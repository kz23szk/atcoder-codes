N = int(input())
A = [0] + list(map(int, input().split()))
# 最後に上がった日にち
save_index = [1]
pos = 2
kisanbi = [-1 for i in range(N + 1)]
while pos <= N:
    # 直前より下がったら無条件で前日が起算日
    if A[pos - 1] > A[pos]:
        kisanbi[pos] = pos - 1
    else:
        for i in save_index[::-1]:
            if A[i] > A[pos]:
                kisanbi[pos] = i
                break
        save_index.append(pos)
    pos += 1

print(*kisanbi[1:])
