n=[]
for i in range(9):
    n.append(int(input()))
m=max(n)
print(m)
print(n.index(m)+1)