N = int(input())
A = list(map(int, input().split()))

avg = sum(A)/len(A)
diffA = [abs(avg - a) for a in A]
diffA = [a for a in diffA if a >=1]

print(int(sum(diffA)//2))