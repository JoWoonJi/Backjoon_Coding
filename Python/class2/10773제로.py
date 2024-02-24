import sys

k = int(input())
stack = []

for _ in range(k):
    n = int(sys.stdin.readline().strip())

    if n != 0:
        stack.append(n)

    if n == 0:
        stack.pop()
print(sum(stack))
#84ms로 빨라졌다.

# //

#첫시도에 바로 맞았지만 시간이 4064ms 오래걸림. 어제 한 괄호문제와 로직은 비슷
# k = int(input())
# stack = []

# for _ in range(k):
#     n = int(input())

#     if n != 0:
#         stack.append(n)

#     if n == 0:
#         stack.pop()
# print(sum(stack))
