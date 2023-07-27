N = int(input())
val = 0
for _ in range(N):
    operator, v = input().split()
    v = int(v)
    if operator == "+":
        val += v

    elif operator == "-":
        val -= v
    else:
        val *= v
    val %= 10000
    print(val)
