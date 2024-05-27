n=int(input())
p=[tuple(map(int,input().split())) for _ in range(n)]
r=[1]*n
for i in range(n):
    for j in range(n):
        if i!=j and p[i][0]<p[j][0] and p[i][1] < p[j][1]:
            r[i]+=1
print(' '.join(map(str,r)))
