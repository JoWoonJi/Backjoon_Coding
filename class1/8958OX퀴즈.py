n = int(input())

for _ in range(n):
    ox = list(input())
    score = 0
    straight = 0
    for i in ox:
        if i == "O":
            straight += 1
            score += straight
        else:
            straight = 0
    print(score)

