N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
min_price = P
for d in D:
    if Q + d < min_price:
        min_price = Q + d
print(min_price)
