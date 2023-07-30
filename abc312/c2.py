import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
B.reverse()


# この値段で買ってくれる人数
def get_buyler_count(price, buyerlist):
    return len([want_price for want_price in buyerlist if want_price >= price])


if A[0] > B[0]:
    print(B[0] + 1)  # 出力例2からこう出力しているがよくわからない
    sys.exit(0)

# 2分木にしないと遅いかも
left = 0
right = N - 1
while right - left > 10:
    mid = (left + right) // 2
    # この値段なら買ってもいい人の人数
    buyer_count = len([price for price in B if price >= A[mid]])
    # 売ってもよいと考える売り手の人数
    seller_count = mid + 1
    if buyer_count <= seller_count:
        right = mid
    else:
        left = mid

for i in range(left, right+1):
    buyer_count = len([price for price in B if price >= A[i]])
    if 0 < buyer_count <= i + 1:
        print(A[i])
        sys.exit(0)
print(B[0] + 1)

