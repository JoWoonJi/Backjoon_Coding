n = int(input())

p = list(map(int, input().split())) #로직은 쉬운데 입력 형태가 헷갈. 
p.sort()
#p = sorted(list(map(int, input().split()))) 
t = 0
a = 0
for i in p:
    t += i
    a += t
print(a)