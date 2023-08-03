N, X, Y = map(int, input().split())
# 最短で(X + Y)回で到達できて、残った回数が偶数ならOK
X = abs(X)
Y = abs(Y)
if X + Y <= N and (N - (X + Y)) % 2 == 0:
    print("Yes")
else:
    print("No")
