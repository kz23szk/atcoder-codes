# 愚直に2分木探索した場合
N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N-1):
    left = i+1
    right = N - 1
    # 一番小さい値との差がKより大きい
    if A[left] - A[i] > K:
        continue
    # 一番大きい値との差がK以下なので全てのペアの分加算
    if A[right] - A[i] <= K:
        count += N - i - 1
        continue
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] - A[i] > K:
            right = mid
        else:
            left = mid
    count += left - i
print(count)
