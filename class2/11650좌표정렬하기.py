#더 간결하게 / 튜플은 기본적으로 문제 조건과 마찬가지로 첫번째 인자 순 정렬 그다음 두번째 인자 정렬을 하기 때문에 문제의 목적은 람다 대신에 튜플을 배우라는 것 같다. 
import sys

n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for x, y in sorted(dots):
    print(x, y)

#//

# #어제 한 나이순 정렬보다 쉬운문제. input 써도 통과되긴하지만 시간이 오래걸려서 sys / sorted써도 빨라서 sorted 람다 기본형으로 쉽게.
# import sys
# n = int(sys.stdin.readline().strip())
# dots = []
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().strip().split())
#     dots.append((x, y))

# dots_sorted = sorted(dots, key=lambda i: (i[0], i[1]))
# for i in dots_sorted:
#     print(i[0], i[1])