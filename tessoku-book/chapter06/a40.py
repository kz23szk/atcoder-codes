N = int(input())
A = list(map(int, input().split()))
line_dict = dict()
for a in A:
    if a not in line_dict:
        line_dict[a] = 1
    else:
        line_dict[a] += 1


# n個からm個選ぶ組み合わせ方を返す
def combination(n, m):
    result = 1
    for i in range(m):
        result *= n - i
    for i in range(2, m + 1):
        result /= i
    return int(result)


pattern_count = 0
for line_count in line_dict.values():
    if line_count >= 3:
        pattern_count += combination(line_count, 3)
print(pattern_count)
