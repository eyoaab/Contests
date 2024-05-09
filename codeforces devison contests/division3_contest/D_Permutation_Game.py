def calculate_score(position, a):
    return a[position - 1]

def simulate_game(n, k, PB, PS, permutation, a):
    Bodya_score = PB
    Sasha_score = PS

    for _ in range(k):
        Bodya_score += calculate_score(Bodya_score, a)
        Sasha_score += calculate_score(Sasha_score, a)
        Bodya_score = permutation[Bodya_score - 1]
        Sasha_score = permutation[Sasha_score - 1]

    if Bodya_score > Sasha_score:
        return "Bodya"
    elif Bodya_score < Sasha_score:
        return "Sasha"
    else:
        return "Draw"

t = int(input())
for _ in range(t):
    n, k, PB, PS = map(int, input().split())
    permutation = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(simulate_game(n, k, PB, PS, permutation, a))
