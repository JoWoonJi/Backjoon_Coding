import math 
n, k = map(int, input().split())
print(math.comb(n,k))

#처음으로 숏코딩에 근접 / 파이썬에서 *연산자는 곱과 argument unpacking(인자 풀기)에 사용
#import math
#print(math.comb(*map(int,input().split())))

# from math import factorial # 이런 간단한 방법이! 수학적인거는 이미 모듈로 구현이 되어있다.

# def binomial_coefficient(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))

# n, k = map(int, input().split())
# print(binomial_coefficient(n, k))

# 팩토리얼을 구현하고 이항계수 공식 적용.
# def binomial_coefficient(n, k):
#     def factorial(x): # 팩토리얼함수. 재귀적. 정처기 기출.
#         if x == 0 or x == 1:
#             return 1
#         return x * factorial(x - 1)
    
#     return factorial(n) // (factorial(k) * factorial(n - k)) #이항 계수 공식 n! / k!*(n-k)!

# n, k = map(int,input().split())
# print(binomial_coefficient(n, k))
