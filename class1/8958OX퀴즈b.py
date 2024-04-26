t=int(input())
for _ in range(t):
    ox=list(input())
    serial=0
    score=0
    for i in ox:
        if i=='O':
            serial+=1
            score+=serial
        else:
            serial=0
    print(score)