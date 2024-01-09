t = int(input())
for _ in range(t):
    k = int(input()) #floor
    n = int(input()) #roomnumber
    rooms = [i for i in range(1, n+1)]
    for j in range(k):
        for l in range(1, n):
            rooms[l] += rooms[l-1]
    print(rooms[-1])
