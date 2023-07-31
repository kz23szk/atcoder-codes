N = int(input())
A = list(map(int, input().split()))
# カードを大きい順に並び替える
A.sort()
A.reverse()

alice_cards = [a for i, a in enumerate(A) if i % 2 == 0]
bob_cards = [a for i, a in enumerate(A) if i % 2 == 1]
print(sum(alice_cards) - sum(bob_cards))
