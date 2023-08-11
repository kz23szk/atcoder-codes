N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
bit = 2 ** N
dp = [[(False, set()) for _ in range(bit)] for _ in range(M+1)]
dp[0][0] = (True, set())

def to_binary_num_list(n, item_num):
    l = []
    while n > 0:
        l.append(n % 2)
        n //= 2
    for i in range(item_num - len(l)):
        l.append(0)
    return l

def to_decimal_num(l):
    n = 0
    for i in range(len(l)):
        if l[i] == 1:
            n += 2 ** i
    return n

# 2進数nとクーポンを使ったときに追加で手に入れられるビットを10進数にして返す
def get_diff(n, coupon, item_num):
    l = []
    items = to_binary_num_list(n, item_num)
    for i in range(item_num):
        if items[i] == 0 and coupon[i] == 1:
            l.append(1)
        else:
            l.append(0)
    return to_decimal_num(l)

for i in range(M):
    for j in range(bit):
        exist, c = dp[i][j]
        c2 = c.copy()
        if exist:
            diff= get_diff(j, A[i], N)
            dp[i+1][j] = (True, c2)
            if j + diff < bit:
                c2.add(i)
                dp[i+1][j+diff] = (True, c2)

for row in dp:
    print(*row)
print(dp[-1][-1])
