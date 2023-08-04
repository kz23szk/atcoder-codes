from collections import deque

S = list(input())
queue = deque()
for i, char in enumerate(S):
    if char == "(":
        queue.append(i + 1)
    else:
        index = queue.pop()
        print(index, i + 1)
