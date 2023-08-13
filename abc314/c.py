N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))
color_index = [-1 for i in range(M + 1)]
count = N
Sindex = [i for i in range(N)]
moved = [ False for i in range(N)]

i = 0
while count > 0:
    if color_index[C[i]] == -1:
        color_index[C[i]] = i
    else:
        if not moved[i]:
            Sindex[i] = color_index[C[i]]
            color_index[C[i]] = i
            count -= 1
            moved[i] = True
    i += 1
    if i == N:
        i = 0

output = "".join([S[i] for i in Sindex])
print(output)
