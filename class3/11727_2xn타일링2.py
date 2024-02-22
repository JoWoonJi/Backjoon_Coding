n=int(input())
d=[0]*(n+1)
d[0],d[1]=1,1
for i in range(2,n+1):
    d[i]=d[i-1]+2*d[i-2]
print(d[n]%10007)

# n = int(input())
# dp = [0] * (n + 1)
# dp[0], dp[1] = 1, 1
# for i in range(2, n + 1):
#     dp[i] = (dp[i - 1] + 2 * dp[i - 2])
# print(dp[n]%10007)