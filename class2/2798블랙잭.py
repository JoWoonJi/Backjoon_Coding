n, m = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(n, m, cards):
    close_made = 0

    for a in range(n - 2):
        for b in range(a + 1, n - 1):
            for c in range(b + 1, n):
                current_sum = cards[a] + cards[b] + cards[c]

                if current_sum == m:
                    return m  
                elif current_sum < m:
                    close_made = max(close_made, current_sum)

    return close_made

result = blackjack(n, m, cards)
print(result)