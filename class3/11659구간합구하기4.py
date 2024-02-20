import sys
input=sys.stdin.readline
n,m=map(int,input().split())
x=list(map(int,input().split()))
s=[0]
for i in x:
    s.append(s[-1]+i)
for _ in range(m):
    i,j=map(int,input().split())
    print(s[j]-s[i-1])


#시간초과
# n, m = map(int, input().split())

# x = list(map(int, input().split()))

# for _ in range(m):
#     i, j = map(int, input().split()) 
#     print(sum(x[i-1:j]))  