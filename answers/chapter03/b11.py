N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())


def count_lower_elem(l, x):
    lower_index = 0
    upper_index = len(l) - 1

    if l[lower_index] > x:
        return 0
    if l[upper_index] < x:
        return len(l)

    while True:
        check_index = (upper_index + lower_index) // 2
        if l[check_index] == x:
            return check_index
        elif l[check_index] < x:
            if len(l) - 1 >= check_index + 1 and x < l[check_index + 1]:
                return check_index + 1
            lower_index = check_index
        else:
            if 0 <= check_index - 1 and l[check_index - 1] < x:
                return check_index
            upper_index = check_index


for i in range(Q):
    print(count_lower_elem(A, int(input())))
