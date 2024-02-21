n=int(input())
d=[0]*1001
d[1]=1
d[2]=2
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n]%10007)


# def t(n):
#     if n <= 1:
#         return n
#     a, b = 1, 2 
#     for i in range(3, n + 1):
#         a, b = b, (a + b) % 10007 
#     return b 

# n = int(input())
# print(t(n))



# def tile_filling(n):
#     if n <= 1:
#         return n
    
#     dp = [0] * (n + 1)
#     dp[1], dp[2] = 1, 2
    
#     for i in range(3, n + 1):
#         dp[i] = (dp[i-1] + dp[i-2]) % 10007 
    
#     return dp[n]

# n = int(input())
# print(tile_filling(n))