N, M = map(int, input().split())
start1 = "###."
start2 = "...."

end1 = "...."
end2 = ".###"

rows = []
for _ in range(N):
    rows.append(input())

for i in range(N-8):
    for j in range(M-8):
        if rows[i][j:j+4] == start1 and rows[i+1][j:j+4] == start1 and rows[i+2][j:j+4] == start1 and rows[i+3][j:j+4] == start2 and \
                rows[i+5][j+5:j + 9] == end1 and rows[i+6][j+5:j + 9] == end2 and rows[i+7][j+5:j + 9] == end2 and  rows[i+8][j+5:j + 9] == end2:
            print(i+1, j+1)





