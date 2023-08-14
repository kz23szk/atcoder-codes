N, K = map(int, input().split())
S = list(map(int, input()))

on_count = len([on_off for on_off in S if on_off == 1])
# 現状のonの数の偶奇とKの偶奇が同じなら可能
print("Yes") if (on_count % 2) == (K % 2) else print("No")