n = int(input())
bags = 0

while n >= 0:
    if n % 5 == 0:
        bags += n // 5
        print(bags)
        break
    n -= 3 # 3을 빼주고 다시 반복문. 
    bags += 1
else:
    print(-1)

#동적 계획법(Dynamic Programming)
# n = int(input())
# dp = [5001] * (n + 1)
# dp[0] = 0

# for i in range(3, n + 1):
#     if i >= 3:
#         dp[i] = min(dp[i], dp[i - 3] + 1)
#     if i >= 5:
#         dp[i] = min(dp[i], dp[i - 5] + 1)

# print(-1 if dp[n] > 5000 else dp[n])
