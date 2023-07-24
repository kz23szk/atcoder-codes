N = int(input())
A = list(map(int, input().split()))
D = int(input())

# 累積maxを格納する配列を定義
maxR = [0] * N
maxL = [0] * N

# 初期値を設定
maxR[0] = A[0]
maxL[N-1] = A[N-1]

# 右から最大値の累積を求める
for i in range(1, N):
    maxR[i] = A[i] if A[i] > maxR[i-1] else maxR[i-1]

# 左から最大値の累積を求める
for i in reversed(range(N-1)):
    maxL[i] = A[i] if A[i] > maxL[i+1] else maxL[i+1]

for _ in range(D):
    L, R = map(int, input().split())
    print(max(maxR[L-2], maxL[R]))

