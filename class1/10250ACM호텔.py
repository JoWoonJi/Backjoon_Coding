t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    floor = n % h 
    distance = (n // h) + 1
    if floor == 0:
        floor = h
        distance -= 1
    print(floor * 100 + distance)