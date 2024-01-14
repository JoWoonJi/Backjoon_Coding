import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
nums.sort()
sys.stdout.write('\n'.join(map(str,nums)))
#join은 문자열 결합에 사용되기때문에 str로 변환. 개행문자와 숫자를 하나의 큰 문자로 결합해서 줄바꿈 출력하는 것
#sys.stdout.write와 print 속도면에서 별 차이가 없다. 

#//

#sys.stdout.write사용,join사용하지 않고. 메모리사용은 반으로 줄었지만 처리시간은 비슷.
# import sys

# n = int(sys.stdin.readline().strip())
# nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
# nums.sort()
# for i in nums:
#     sys.stdout.write(str(i) + '\n')

#//

# 첫번째 시도 시간초과 / 수정렬하기3와 같은 방식이기에 했던대로 sys 사용
# n = int(input())
# nums = []
# for _ in range(n):
#     num = int(input())
#     nums.append(num)

# nums.sort()
# for i in nums:
#     print(i)

