
#수정렬하기때 배웠던 strip()활용. 오른쪽은 rstrip/왼쪽은lstrip
from math import factorial

n = int(input())

n_fac_str = str(factorial(n))
n_fac_trimmed = n_fac_str.rstrip('0')
count = len(n_fac_str) - len(n_fac_trimmed)

print(count)

# from math import factorial

# n = int(input())

# n_fac = factorial(n)
# count = 0

# # 팩토리얼 결과를 문자열로 변환
# n_fac_str = str(n_fac)

# # 문자열의 끝에서부터 '0'이 아닌 숫자를 만날 때까지 순회
# for char in reversed(n_fac_str):
#     if char == '0':
#         count += 1
#     else:
#         break

# print(count)


