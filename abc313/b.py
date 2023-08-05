import sys

N, M = map(int, input().split())

# 出てきた人を入れておく
appears = set()
relations= []
for i in range(M):
    a, b = map(int, input().split())
    appears.add(a)
    appears.add(b)
    relations.append((-1, a, b))

for i in range(M):
    strong1, a1, b1 = relations[i]
    for j in range(M):
        if i != j:
            strong2, a2, b2 = relations[j]
            if a1 == b2:
                relations[i] = (j, a1, b2)


count = 0
index = -1
saikyo = set()
for r in relations:
    s, a, b = r
    if s == -1:
        saikyo.add(a)
if len(saikyo) == 1 and len(appears) == N:
    saikyo_a = None
    for s in saikyo:
        saikyo_a = s

    saikyo_b = []
    if len(relations) > 1:
        for i, r in enumerate(relations):
            s, a, b = r
            if s == -1:
                saikyo_b.append((i, b))
                for i2, r2 in enumerate(relations):
                    s2, a2, b2 = r2
                    if i != i2 and a2 == b:
                        flag = True
                if flag == False:
                    print(-1)
                    sys.exit(0)

    print(saikyo_a)
else:
    print(-1)