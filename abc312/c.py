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


for i in range(N):
    # print(A[i], B, get_buyler_count(A[i], B))
    buyer_count = get_buyler_count(A[i], B)
    if buyer_count > 0 and i + 1 >= get_buyler_count(A[i], B):
        print(A[i])
        sys.exit(0)
print(B[0] + 1)  # 出力例2からこう出力しているがよくわからない
