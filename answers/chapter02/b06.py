N = int(input())
A = list(map(int, input().split()))
Q = int(input())

Atotalwin = [0]
Atotallose = [0]
for a in A:
    if a == 1:
        Atotalwin.append(Atotalwin[-1] + 1)
        Atotallose.append(Atotallose[-1])
    else:
        Atotalwin.append(Atotalwin[-1])
        Atotallose.append(Atotallose[-1] + 1)

for n in range(Q):
    L, R = map(int, input().split())
    wincnt = Atotalwin[R] - Atotalwin[L - 1]
    losecnt = Atotallose[R] - Atotallose[L - 1]
    if wincnt > losecnt:
        print("win")
    elif wincnt == losecnt:
        print("draw")
    else:
        print("lose")
