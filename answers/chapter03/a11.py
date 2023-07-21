N, X = map(int, input().split())
A = list(map(int, input().split()))

lower_index = 0
upper_index = N
check_index = 0
while True:
    check_index = (upper_index + lower_index) //2
    if A[check_index] == X:
        break
    elif A[check_index] < X:
        lower_index = check_index
    else:
        upper_index = check_index

print(check_index + 1)
