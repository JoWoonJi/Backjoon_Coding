import math #math는 기본 표준라이브러리라 백준에서 사용가능 / sys는 속도차이가 없음

m, n = map(int, input().split())

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1): #math 라이브러리의 sqrt 함수를 사용하여 주어진 수의 제곱근까지만 반복하여 나누어 보고, 나누어떨어지는 수가 없다면 그 수를 소수로 판단
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if prime(i):
        print(i)

# //        

#sympy라는 외부라이브러리를 활용하면 소수를 간단하게 구할 수 있다. 하지만 백준 실행환경에서는 이 라이브러리를 사용할수 없으므로.
# from sympy import primerange

# M, N = map(int, input().split())

# primes = list(primerange(M, N+1))

# for prime in primes:
#     print(prime)
        
# //        

# #전에 했던 1978 소수찾기 로직. 이 로직으로 하면 시간초과        
# M, N = map(int, input().split())

# # M부터 N까지의 모든 수에 대해 소수인지 판별
# for i in range(M, N + 1):
#     # 1은 소수가 아니므로 건너뜀
#     if i > 1:
#         for j in range(2, i):
#             # i가 j로 나누어 떨어지면 소수가 아님
#             if i % j == 0:
#                 break
#         else:
#             # for-else 구문을 사용, 내부 for 반복문에서 break에 걸리지 않았다면 i는 소수
#             print(i)