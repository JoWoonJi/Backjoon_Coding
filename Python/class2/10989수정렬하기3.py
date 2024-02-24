import sys

def efficient_counting_sort():
    num_list = [0] * 10001
    n = int(sys.stdin.readline().strip()) 
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        num_list[num] += 1

    for i in range(10001):
        if num_list[i] != 0:
            for _ in range(num_list[i]):
                sys.stdout.write(str(i) + '\n')

efficient_counting_sort()
# 아래가 더 빠를것같은데 이상하게 함수 정의한것이 2000ms(2초) 정도 더 빠르다. gpt도 함수정의한것이 유의미한 차이는 없지만 느릴수있다고 하는데 실제 결과는 반대.

# import sys

# n = int(sys.stdin.readline().strip())
# num_list = [0] * 10001

# for _ in range(n):
#     num = int(sys.stdin.readline().strip())
#     num_list[num] += 1
# for i in range(10001):
#     if num_list[i] != 0:
#         for _ in range(num_list[i]):
#             sys.stdout.write(str(i) + '\n')


# strip() 함수는 문자열 양 끝의 공백이나 개행 문자를 제거

#첫시도 . 시간이 오래 걸리고 메모리 초과가 됨
# n = int(input())  
# numbers = []

# for _ in range(n):
#     num = int(input())
#     numbers.append(num)

# sorted_numbers = sorted(numbers)

# for num in sorted_numbers:
#     print(num)

# //


# 다른 답. 큰 차이는 없고 sys.stdin.readline는 사용하면서 sys.stdout.write는 사용하지 않음.
# import sys
# input=sys.stdin.readline

# N = int(input()) # 수의 개수

# num = [0] * 10001

# for _ in range(N) :
#     temp = int(input())
#     num[temp] += 1

# for i in range(10001) :
#     if num[i] != 0 :
#         for j in range(num[i]) :
#             print(i)

