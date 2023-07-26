_, x = map(int, input().split())
isXs = [a == x for a in map(int, input().split())]
print("Yes") if max(isXs) else print("No")
