N, Q = map(int, input().split())

A = [i + 1 for i in range(N)]
reverse = False
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if reverse:
            A[N - q[1]] = q[2]
        else:
            A[q[1] - 1] = q[2]
    elif q[0] == 2:
        reverse = not reverse
    elif q[0] == 3:
        if reverse:
            print(A[N - q[1]])
        else:
            print(A[q[1] - 1])
