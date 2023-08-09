N, L = map(int, input().split())
A, B = [0 for _ in range(N)], ["" for _ in range(N)]
for i in range(N):
    a, b = input().split()
    A[i] = int(a)
    B[i] = b

# それぞれがトンネルを出る時間を出す
max_sec = 0
for i in range(N):
    sec = 0
    if B[i] == 'E':
        sec = L - A[i]
    else:
        sec = A[i]
    if sec > max_sec:
        max_sec = sec

print(max_sec)
