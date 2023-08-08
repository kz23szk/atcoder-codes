d = dict()
Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        d[q[1]] = int(q[2])
    elif q[0] == '2':
        print(d[q[1]])
