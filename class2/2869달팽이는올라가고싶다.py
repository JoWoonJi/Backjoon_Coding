a, b, v = map(int ,input().split())
x = (v - b) / (a - b)
if x == int(x):
    print(int(x)) #파이썬은 나눗셈의 결과는 float실수형으로 출력해버리기때문에 같은 값이어도 정수형으로 변환
else:
    print(int(x) + 1)


# a, b, v = map(int,input().split())
# def climbing_days(a, b, v):
#     adjusted_height = v - b # 올라야 하는 총 높이. 그냥 정상 올랐다 치고 b를 빼버리면 하루를 더할 필요가 없다.
#     effective_climb = a - b # 하루동안 실제 오르는 높이
#     days = adjusted_height // effective_climb # 필요한 전체 날짜 수

#     if adjusted_height % effective_climb != 0:  # 나누어떨어지지 않으면 하루가 더필요한거기 때문에 +1 해줘야함
#         days += 1

#     return days # a를 뺄 때와 다르게 b를 뺐기 때문에 1을 더할 필요가 없다 .
# print(climbing_days(a, b, v))

# a, b, v = map(int,input().split())
# def climbing_days(a, b, v):
#     adjusted_height = v - a # 올라야 하는 총 높이. a를 미리 빼주는 이유는 마지막날 a 올라가면 미끄러지지 않기 때문.
#     effective_climb = a - b # 하루동안 실제 오르는 높이
#     days = adjusted_height // effective_climb # 필요한 전체 날짜 수

#     if adjusted_height % effective_climb != 0:  # 나누어떨어지지 않으면 하루가 더필요한거기 때문에 +1 해줘야함
#         days += 1

#     return days + 1 #a 만큼 미리 빼주었기 때문에 +1 해주고 마무리.
# print(climbing_days(a, b, v))


# A, B, V = map(int ,input().split())
# x = (V - B) / (A - B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)

