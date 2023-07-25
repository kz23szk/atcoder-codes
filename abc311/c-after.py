import sys

N = int(input())
B = [0] + list(map(int, input().split()))

start_points = B.copy()
while len(start_points) > 1:
    root = [start_points[-1]]
    start_points.pop(-1)
    for j in range(N):
        check_index = root[-1]
        if B[check_index] in root:
            start = root.index(B[check_index])
            print(len(root[start:]))
            print(" ".join([str(i) for i in root[start:]]))
            sys.exit(0)
        else:
            root.append(B[check_index])
            start_points.remove(B[check_index])
