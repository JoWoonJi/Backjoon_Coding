#어제 한 코드에서 x y 정렬순서만 바꾸면되므로 람다에서 인자 순서만 바꿨다. 쉬운문제
import sys
n = int(sys.stdin.readline().strip())
dots = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    dots.append((x, y))

dots_sorted = sorted(dots, key = lambda i : (i[1], i[0]))
for x, y in dots_sorted:
    print(x, y)

#//

#어제 했던 튜플 방식으로 하려면 x,y 순서를 -1로 거꾸로 저장하고 출력할때 다시 바꿔주면 된다
# n = int(sys.stdin.readline().strip())

# dots = [tuple(map(int, sys.stdin.readline().strip().split()))[::-1] for _ in range(n)]

# for y, x in sorted(dots):
#     print(x, y)