#함수 없이. 이진탐색이 find보다 효율적인 이유는 정렬된 배열에서는 범위를 반씩 줄여나가며 위치를 특정하기 때문. find는 전체를 다 찾아야 하므로 느려짐.
from bisect import bisect_left
import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
search = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in search:
    index = bisect_left(a, i)
    if index < n and a[index] == i: #bisect 함수라서 index < n 가 필요하다. 만약에 [1,3,5]이고 search값이 bisect_left(a, 6) 이라면 6이 배열 안에 들어가서 위치를 특정해야하는데 배열을 넘어서는 인덱스이기 때문에 오류가 남.
        print(1)
    else:
        print(0)

# # 함수 정의
# from bisect import bisect_left, bisect_right # bisect는 이진탐색 알고리즘, 정렬된 배열에서 특정원소 위치 찾을때 활용

# def exists_in_array(arr, x):
#     index = bisect_left(arr, x)
#     if index < len(arr) and arr[index] == x:
#         return 1  
#     return 0  

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# queries = list(map(int, input().split()))

# a.sort()

# for i in queries:
#     print(exists_in_array(a, i))