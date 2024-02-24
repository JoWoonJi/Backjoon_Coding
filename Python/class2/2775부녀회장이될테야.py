t = int(input())
for _ in range(t):
    k = int(input()) #floor
    n = int(input()) #roomnumber
    rooms = [i for i in range(1, n+1)] #rooms[0] = 1 rooms[1] = 2 이런식 
    for j in range(k):
        for l in range(1, n): # 1은 처음부터 초기화 되어서 들어가있음. rooms[0] = 1 의 값은 고정. n이 4라면 rooms[1] rooms[2] rooms[3] 까지만 집어넣는것. 그래서 n+1까지가 아닌 n까지.
            rooms[l] += rooms[l-1]
    print(rooms)
