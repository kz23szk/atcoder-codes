H, W, N = map(int, input().split())
cells = [[ 1 for i in range(W)] for j in range(H)]

# 穴を開ける
for _ in range(N):
    a, b = map(int, input().split())
    cells[a-1][b-1] = 0

# 正方形を数える
# print(cells)

min_index = min(H, W)
count = 0
for i in range(1, min_index+1):
    for h in range(H):
        cutCells = cells[h:h+i]
        # print(cutCells)
        for j in range(W):
            same_cnt = 0
            for c in cutCells:
                # print(i, sum(c[j:j+i]))
                if i == sum(c[j:j+i]):
                    same_cnt += 1
            if same_cnt == i:
                # print("up")
                count += 1

print(count)
