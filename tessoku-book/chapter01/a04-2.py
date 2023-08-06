N = int(input())
num_list = []
while N > 0:
    num_list.append(N % 2)
    N //= 2

if len(num_list) < 10:
    num_list += [0] * (10 - len(num_list))

num_list.reverse()
print(*num_list, sep="")
