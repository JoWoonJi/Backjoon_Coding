a, b = map(int,input().split())
gcd_list = []
for i in range(1, min(a,b) + 1): 
    if a % i == 0 and b % i == 0:
        gcd_list.append(i)
# 리스트 컴프리헨션 :gcd_list = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
        
print(max(gcd_list))

a_multi = {a * i for i in range(1, b+1)} #리스트 [] 아님 딕셔너리{'a': 1, 'b': 2} 아님 / set {1, 2, 3} 임
b_multi = {b * j for j in range(1, a+1)}

common_elements = a_multi.intersection(b_multi)  #교집합 익히기

if common_elements:
    lcm = min(common_elements)
    print(lcm)
else:
    print(a*b)



#리스트 컴프리헨션 사용 
# a, b = map(int, input().split())

# # 최대공약수(GCD) 계산
# gcd_list = []
# for i in range(1, min(a,b) + 1):  # 범위를 min(a, b)로 변경
#     if a % i == 0 and b % i == 0:
#         gcd_list.append(i)  # 공약수 추가
        
# print(max(gcd_list))

# # 최소공배수(LCM) 계산
# a_multi = [a * i for i in range(1, b+1)]
# b_multi = [b * j for j in range(1, a+1)]

# # 공통 요소 찾기
# lcm = min([i for i in a_multi if i in b_multi])
# print(lcm)

#//

#유클리드 호제법, gcd lcm관계 이용 
# a, b = map(int, input().split())

# # 최대공약수(GCD) 계산
# def compute_gcd(x, y):
#    while(y):
#        x, y = y, x % y
#    return x

# gcd = compute_gcd(a, b)
# print(gcd)

# # 최소공배수(LCM) 계산
# def compute_lcm(x, y):
#    lcm = (x*y)//compute_gcd(x,y)
#    return lcm

# lcm = compute_lcm(a, b)
# print(lcm)