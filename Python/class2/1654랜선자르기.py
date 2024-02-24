# 간결하게
import sys
input=sys.stdin.readline
k,n=map(int,input().split())
c=[int(input()) for _ in range(k)]
a,z=1,max(c)
while a<=z:
    m=(a+z)//2
    if sum(i//m for i in c)>=n:
        a=m+1 
    else:
        z=m-1
print(z)

# import sys
# input = sys.stdin.readline

# k, n = map(int, input().split()) 
# cables = [int(input()) for _ in range(k)] 

# a, z = 1, max(cables) 

# while a <= z:
#     mid = (a + z) // 2 

#     if sum(i // mid for i in cables) >= n: 
#         a = mid + 1 
#     else: 
#         z = mid - 1 

# print(z)
