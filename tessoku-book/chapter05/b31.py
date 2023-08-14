N = int(input())

x3 = N // 3
x5 = N // 5
x7 = N // 7

x15 = N // 15
x35 = N // 35
x21 = N // 21

x105 = N // 105

print(x3 + x5 + x7 - x15 - x35 - x21 + x105)
