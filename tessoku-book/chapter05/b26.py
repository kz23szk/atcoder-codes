# エラトステネスのふるい
N = int(input())
# そのインデックスが素数であるかを格納する配列
candidate = [True for i in range(N + 1)]
candidate[0] = False
candidate[1] = False
index = 2
while index < N ** 0.5:
    if candidate[index] == True:
        for i in range(2, N // index + 1):
            candidate[index * i] = False
    index += 1
for i in range(2, N + 1):
    if candidate[i]:
        print(i)
