def m(n):
    while n%4==0:
        n//=4
    if n%8==7:
        return 4
    if int(n**0.5)**2==n:
        return 1
    for i in range(1, int(n**0.5)+1):
        if int((n-i*i)**0.5)**2==n-i*i:
            return 2
    return 3
n=int(input())
print(m(n))

# #시간초과
# n = int(input())

# dp = [0] * (n + 1)

# for i in range(1, n + 1):
#     dp[i] = i 
#     j = 1
#     while j**2 <= i:
#         dp[i] = min(dp[i], dp[i - j**2] + 1)
#         j += 1

# print(dp[n])
