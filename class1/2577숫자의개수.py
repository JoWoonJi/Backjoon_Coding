# count 내장함수 없이 직접 함수 만들기
def countfunction(a, b, c):
    result = list(str(a * b * c))
    counterpunch = [0] * 10
    for i in result:
        counterpunch[int(i)] += 1
    return counterpunch

#한줄씩 입력
a = int(input())
b = int(input())
c = int(input())

counterpunch = countfunction(a, b, c)
for i in range(10):
  print(counterpunch[i])

'''count 내장함수 활용
a = int(input())                # 150
b = int(input())                # 266
c = int(input())                # 427
result = list(str(a * b * c))   # [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10):             # i = 0 ~ 9
    print(result.count(str(i))) # i를 문자열(str)로 바꿔서 몇 개 있는지 count함
'''