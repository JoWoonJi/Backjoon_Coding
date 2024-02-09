import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = set(input().strip() for _ in range(n))
w = set(input().strip() for _ in range(m))

r = sorted(l & w)

print(len(r))
print('\n'.join(r))


#처음에 이렇게 짰는데 시간초과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# l, w = [], []
# for _ in range(n):
#     l.append(input().strip())
# for _ in range(m):
#     w.append(input().strip())

# r = []
# for i in l:
#     for j in w:
#         if i == j: 
#             r.append(i)
# r.sort()
# print(len(r))
# print('\n'.join(r))

#집합과 리스트의 차이
# set의 교집합 연산이 리스트의 각 요소를 순회하며 비교하는 방식보다
# 훨씬 효율적인 이유는 set의 내부 구현 방식 때문입니다.
# set은 해시 테이블을 기반으로 구현되어 있어서,
# 평균적인 경우 요소의 존재 여부를 상수 시간 O(1)내에 확인할 수 있습니다.
# 따라서 set을 사용하여 두 집합의 교집합을 구하는 연산은
# 두 집합의 크기에 비례하는 시간이 걸립니다.
# 이는 리스트를 사용할 때 각 요소를 모두 순회하며 비교하는
# O(N×M)의 시간 복잡도보다 훨씬 빠릅니다.