import sys

N = int(input())
B = [0] + list(map(int, input().split()))

for i, b in enumerate(B):
    if i > 0:
        root = [i]
        for j in range(N):
            check_index = root[-1]
            if B[check_index] in root:
                start = root.index(B[check_index])
                print(len(root[start:]))
                print(" ".join([str(i) for i in root[start:]]))
                sys.exit(0)
            else:
                root.append(B[check_index])
