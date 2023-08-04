Q = int(input())
queries = [input().split() for _ in range(Q)]
grades = dict()
for q in queries:
    if q[0] == '1':
        grades[q[1]] = q[2]
    elif q[0] == '2':
        print(grades[q[1]])
